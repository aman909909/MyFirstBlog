from django.contrib import admin
from .models import blog
from .models import UserProfile
# Register your models here.

admin.site.register(blog)
admin.site.register(UserProfile)
