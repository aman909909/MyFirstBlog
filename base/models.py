from django.db import models
from datetime import datetime


class blog(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    content=models.TextField()
    date =models.DateTimeField(auto_now_add=True)

