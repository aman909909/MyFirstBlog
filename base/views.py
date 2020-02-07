from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import blog
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'base/home.html')

def new(request):
    return render(request,'base/add.html')

def sub(request):
    if request.method=="POST":
        bg=blog()
        bg.name=request.POST['name']
        bg.email=request.POST['email']
        bg.subject=request.POST['subject']
        bg.content=request.POST['msg']
        bg.save()
        messages.success(request,'Your blog has been posted!')
        return render(request,'base/home.html')
    else:
        return HttpResponse('Wrong')
        
@login_required
def show(request):
    blogs=blog.objects.all()
    return render(request,'base/show.html',{
        'blogs':blogs
    })
