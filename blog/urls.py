
from django.contrib import admin
from django.urls import path, include
from base import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include(urls)),
  
]
