# google_drive.py
import os
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.file']

CLIENT_SECRET_FILE = 'backend/checking_media_gdrive/client_secret_219216437180-eetq9rn7l4he7r025t8vcdf356fhn8p7.apps.googleusercontent.com.json'  # Update this path

def authenticate_google_drive():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return build('drive', 'v3', credentials=creds)

def upload_file_to_drive(file_path):
    service = authenticate_google_drive()
    media = MediaFileUpload(file_path, mimetype='image/jpeg/png')  # Adjust mime type if needed
    file_metadata = {'name': os.path.basename(file_path)}
    
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get("id")

upload_file_to_drive('backend/checking_media_gdrive/test.png')