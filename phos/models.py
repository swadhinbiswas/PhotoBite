from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ImageUploader(models.Model):
    photo=models.ImageField(upload_to='IMAGESTORE/')
    date=models.DateTimeField(auto_now_add=True)

    

class Uploader(models.Model):
    uploadr=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.uploadr
