from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse,Http404
from django.db.models import Q
from .models import blog
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request,'base/home.html')


@login_required(login_url='login_page')
def new(request):
    return render(request,'base/add.html')


@login_required(login_url='login_page')
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
        
        
@login_required(login_url='login_page')
def show(request):
    bg=blog()
    blogs=blog.objects.all().order_by('-id')
    dt=bg.date
    return render(request,'base/show.html',{
        'blogs':blogs,
        'dt':dt
    })

@login_required(login_url='login_page')
def showdetail(request,k):
    blogs=get_object_or_404(blog,pk=k)
    return render(request,'base/show_detail.html',{'blog':blogs})

def delp(request,z):
    zz=get_object_or_404(blog,id=z)
    return render(request,'base/delete.html',{'bg':zz})


def delete(request,z):
    if request.method=="POST":

         zz=get_object_or_404(blog,pk=z)
         zz.delete()
         blogs=blog.objects.all().order_by('-id')
         return render(request,'base/show.html',{
            'blogs':blogs
         })

def search(request):
    qu=request.GET['q']
    try:
        blogs=blog.objects.all().filter(subject__icontains=qu)
    except blog.DoesNotExist:
        raise Http404("No post found!")
    return render(request,'base/show.html',{'blogs':blogs})

def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request,'Username or Password incorrect')
            return render(request,'base/login.html')
    return render(request,'base/login.html')


def signup(request):
    form= CreateUserForm()
    if request.method=="POST":
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+user)
            return redirect('login_page')
    context = {'form':form}
    return render(request,'base/signup.html',context)

def logoutUser(request):
    logout(request)
    return render(request,'base/login.html')
