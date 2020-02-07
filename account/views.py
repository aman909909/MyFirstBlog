from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    next = request.GET.get('next')
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.clened_data.get('username')
        password=form.clened_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect('/')
    context={
        'from':form,
    }
    return render(request,'login.html',context)

# Create your views here.
