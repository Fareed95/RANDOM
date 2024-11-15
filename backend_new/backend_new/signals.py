from django.db.models.signals import post_save
from django.dispatch import receiver
from checking_media_gdrive.models import Image
from .google_drive import upload_to_drive  # Import the refactored utility function

@receiver(post_save, sender=Image)
def upload_image_to_drive(sender, instance, created, **kwargs):
    """
    Signal to automatically upload the image to Google Drive when an Image instance is created.
    """
    if created and instance.image_file:
        # Upload the image to Google Drive
        file_path = instance.image_file.path
        drive_file_id = upload_to_drive(file_path, instance.name)

        # Update the model with the Google Drive file ID
        instance.drive_file_id = drive_file_id
        instance.save()
