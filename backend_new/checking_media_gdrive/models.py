# models.py
from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='images/')  # Local file storage
    drive_file_id = models.CharField(max_length=255, blank=True, null=True)  # Google Drive file ID

    def __str__(self):
        return self.name
