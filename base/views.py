from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse,Http404
from django.db.models import Q
from .models import blog, UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from passlib.hash import pbkdf2_sha256
from django.core.files.storage import FileSystemStorage
# Create your views here.
@login_required(login_url='login_page')
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
    if request.user.is_authenticated:
        return redirect('home_page')
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
    if request.user.is_authenticated:
        return redirect('home_page')

    
    if request.method=="POST":
        name=request.POST['username']
        el=request.POST['email']
        #up_file = request.FILES['profile_photo']
        #fs = FileSystemStorage()
        #fs.save(up_file.name,up_file)
        
        pwd1=request.POST['password1']
        pwd2=request.POST['password2']
        try:
            user = User.objects.get(username=name)
        except :
            
            #if pwd1 != pwd2:
              #  messages.info(request,"Passwords don't match!")
               # return render(request,'base/signup.html')
            if len(pwd1) <2:
                messages.info(request,"Minimum size of password is 8!")
                return render(request,'base/signup.html')
            us=User(username=name,email=el)
            us.set_password(pwd1)
            us.save()
            

            p=UserProfile()
            user = User.objects.get(username=name)
            p.user=user
            p.img = request.FILES['profile']
            p.location=request.POST['location']
            p.save()
            
         
            
            messages.success(request,'Account created')
            return redirect('login_page')
        else :
            messages.info(request,'Username already exists!')
            return render(request,'base/signup.html')
    return render(request,'base/signup.html')

def logoutUser(request):
    logout(request)
    return render(request,'base/login.html')

def profile(request,z):
    user = User.objects.get(pk=z)
    print(user.userprofile.img.url)
    zz=get_object_or_404(User,pk=z)
    return render(request,'base/profile.html',{
      #  'val':zz
    })


    
