from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth,User
from .forms import userregistrationform
# Create your views here.

def register(request):
    
    if request.method=="POST":
       
       form = userregistrationform(request.POST)
       if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email=form.cleaned_data['email']
        bio=form.cleaned_data['bio']
        user = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        passwordtwo = form.cleaned_data['password2']
        authenticate(request,username=user,password=password,email=email)
        form.save()
        return redirect('/')
    else:
        form=userregistrationform()
    context={
        "form":form
    }
    return render(request, 'authtemplates/register.html',context)

def login(request):
    if request.method=="POST":

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    else:
        print('user does not exist')

    context={}
    return render(request, 'authtemplates/login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')