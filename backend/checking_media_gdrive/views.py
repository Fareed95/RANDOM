# views.py
import os
import io
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload

# Google Drive Settings
SCOPES = ['https://www.googleapis.com/auth/drive']
PARENT_FOLDER_ID = "1LNHnS8sy-S0itUQr0QGbEl-2t3lMAvh6"  # Change to your folder ID

def authenticate():
    service_account_info = {
        "type": os.getenv("GDRIVE_TYPE"),
        "project_id": os.getenv("GDRIVE_PROJECT_ID"),
        "private_key_id": os.getenv("GDRIVE_PRIVATE_KEY_ID"),
        "private_key": os.getenv("GDRIVE_PRIVATE_KEY").replace('\\n', '\n'),
        "client_email": os.getenv("GDRIVE_CLIENT_EMAIL"),
        "client_id": os.getenv("GDRIVE_CLIENT_ID"),
        "auth_uri": os.getenv("GDRIVE_AUTH_URI"),
        "token_uri": os.getenv("GDRIVE_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("GDRIVE_AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("GDRIVE_CLIENT_X509_CERT_URL"),
    }
    creds = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    return creds

def upload_photo(file_path, file_name):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': file_name,
        'parents': [PARENT_FOLDER_ID]
    }

    media = MediaFileUpload(file_path, mimetype='image/jpeg')  # Adjust mimetype based on image type

    file = service.files().create(
        body=file_metadata,
        media_body=media
    ).execute()

    return file.get('id')  # Return the file ID from Google Drive


class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('image')
        if not file:
            return Response({"error": "No image uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new Image object to store metadata
        image = Image.objects.create(name=file.name, image_file=file)
        
        # Upload the image to Google Drive
        file_path = image.image_file.path
        drive_file_id = upload_photo(file_path, image.name)

        # Update the Image object with the Google Drive file ID
        image.drive_file_id = drive_file_id
        image.save()

        return Response(ImageSerializer(image).data, status=status.HTTP_201_CREATED)


class ImageRetrieveView(APIView):
    def get(self, request, file_id, *args, **kwargs):
        try:
            image = Image.objects.get(drive_file_id=file_id)
        except Image.DoesNotExist:
            return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the file from Google Drive
        creds = authenticate()
        service = build('drive', 'v3', credentials=creds)
        file = service.files().get(fileId=file_id, fields='name, mimeType').execute()

        file_name = file['name']
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()

        fh.seek(0)
        response = HttpResponse(fh, content_type=file['mimeType'])
        response['Content-Disposition'] = f'attachment; filename={file_name}'

        return response
