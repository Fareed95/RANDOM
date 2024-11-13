import os
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive']
PARENT_FOLDER_ID = "1LNHnS8sy-S0itUQr0QGbEl-2t3lMAvh6"


def authenticate():
    # Create the service account info dictionary from environment variables
    # print("GOOGLE_PRIVATE_KEY:", os.getenv("GDRIVE_PRIVATE_KEY"))  # This should print the key if loaded correctly
    service_account_info = {
    "type": os.getenv("GDRIVE_TYPE"),
    "project_id": os.getenv("GDRIVE_PROJECT_ID"),
    "private_key_id": os.getenv("GDRIVE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GDRIVE_PRIVATE_KEY").replace('\\n', '\n'),  # Convert literal \n to actual newlines
    "client_email": os.getenv("GDRIVE_CLIENT_EMAIL"),
    "client_id": os.getenv("GDRIVE_CLIENT_ID"),
    "auth_uri": os.getenv("GDRIVE_AUTH_URI"),
    "token_uri": os.getenv("GDRIVE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("GDRIVE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("GDRIVE_CLIENT_X509_CERT_URL"),
}


    # Use the service account info to create credentials
    creds = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    return creds

def upload_photo(file_path,file_name):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': file_name,
        'parents': [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()
    
    print(f"File uploaded successfully with ID: {file.get('id')}")

# Example usage:
upload_photo("checking_media_gdrive/test.png","fareed")
