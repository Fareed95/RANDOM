from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer
from backend_new.google_drive import upload_to_drive, download_from_drive


class ImageView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Upload an image to Google Drive and save metadata in the database.
        """
        file = request.FILES.get('image')
        if not file:
            return Response({"error": "No image uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new Image object to store metadata
        image = Image.objects.create(name=file.name, image_file=file)
        
        # Upload the image to Google Drive
        file_path = image.image_file.path
        drive_file_id = upload_to_drive(file_path, image.name)

        # Update the Image object with the Google Drive file ID
        image.drive_file_id = drive_file_id
        image.save()

        return Response(ImageSerializer(image).data, status=status.HTTP_201_CREATED)

    def get(self, request, file_id=None, *args, **kwargs):
        """
        Retrieve an image by its Google Drive file ID or list all images if no file_id is provided.
        """
        if file_id:
            # Fetch a specific image by file_id
            try:
                image = Image.objects.get(drive_file_id=file_id)
            except Image.DoesNotExist:
                return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)

            try:
                # Download the file from Google Drive
                file_content, file_metadata = download_from_drive(file_id)
                mime_type = file_metadata.get('mimeType', 'application/octet-stream')

                # Return the image data as a response
                return HttpResponse(file_content, content_type=mime_type)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            # List all images if no file_id is provided
            images = Image.objects.all()
            data = [
                {
                    "name": image.name,
                    "file_id": f'/api/image/{image.drive_file_id}',
                    "uploaded_at": image.uploaded_at.isoformat() if hasattr(image, 'uploaded_at') else None
                }
                for image in images
            ]
            return Response(data, status=status.HTTP_200_OK)
