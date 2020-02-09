from django.shortcuts import render, get_object_or_404
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
        

def show(request):
    bg=blog()
    blogs=blog.objects.all()
    dt=bg.date
    return render(request,'base/show.html',{
        'blogs':blogs,
        'dt':dt
    })


def showdetail(request,k):
    blogs=get_object_or_404(blog,pk=k)
    return render(request,'base/show_detail.html',{'blog':blogs})

def delete(request,z):
    zz=get_object_or_404(blog,pk=z)
    zz.delete()
    blogs=blog.objects.all().order_by('-id')
    return render(request,'base/show.html',{
        'blogs':blogs
    })

def search(request):
    qu=request.GET['q']
    blogs=blog.objects.all().filter(content__icontains=qu)
    return render(request,'base/show.html',{'blogs':blogs})