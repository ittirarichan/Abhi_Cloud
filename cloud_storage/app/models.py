from django.db import models

# Create your models here.
class Cloud(models.Model):
    img=models.FileField()
    audio=models.FileField()
    video=models.FileField()
    text=models.FileField