from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Check if variables are loaded
print("GOOGLE_PRIVATE_KEY:", os.getenv("GDRIVE_PRIVATE_KEY"))  # This should print the key if loaded correctly
