from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class blog(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    content=models.TextField()
    date =models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profilepic',default='abc.jpeg')
    location = models.CharField(max_length=50, default='abc')
    def save_image(self, *args, **kwargs):
        image = Image.open(self.image.path)
        image.save(self.image.path, quality=10, optimize=True)
        return self
