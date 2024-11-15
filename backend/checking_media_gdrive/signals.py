# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Image
from .views import upload_photo

@receiver(post_save, sender=Image)
def upload_image_to_drive(sender, instance, created, **kwargs):
    if created and instance.image_file:
        # Upload the image to Google Drive
        file_path = instance.image_file.path
        drive_file_id = upload_photo(file_path, instance.name)
        
        # Update the model with the Google Drive file ID
        instance.drive_file_id = drive_file_id
        instance.save()
