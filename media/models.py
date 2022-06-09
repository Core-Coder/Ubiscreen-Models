from django.db import models
from user.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class Media(models.Model):

    class MonetizationStatus(models.IntegerChoices):
        On = 1
        Off = 2

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    monetization_status = models.IntegerField(default='2', choices=MonetizationStatus.choices)
    video = models.FileField(upload_to='videos_uploaded',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    dimension = models.CharField(max_length=100, blank=True, verbose_name="Dimension (Auto)")
    size = models.CharField(max_length=100, blank=True, verbose_name="Size (Auto)")
    duration = models.IntegerField(default=0, verbose_name='Duration in seconds (Auto)')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    media = models.ManyToManyField(Media, blank=True)
    length = models.IntegerField(default=0, verbose_name='Length in seconds (Auto)')
    last_updated = models.DateTimeField(auto_now_add=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'