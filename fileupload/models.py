from django.db import models
from uuid import uuid4
# Create your models here.

def upload_to(instance,filename):
    file_data = filename.split(".")
    filename = str(uuid4())+"."+file_data[-1]
    return 'images/{filename}'.format(filename= filename)


class FileUpload(models.Model):
    """Model definition for FileUpload."""
    image_url = models.ImageField(upload_to=upload_to, max_length=255)


    def __str__(self):
        """Unicode representation of FileUpload."""
        return self.image_url.url

