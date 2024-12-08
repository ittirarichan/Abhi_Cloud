from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def cloud_login(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        data=authenticate(username=username,password=password)
        if data:
            login(req,data)
            return redirect(cloud_home)
        else:
            messages.warning(req, "Invalid username or password.")
            return redirect(cloud_login)
    else:
        return render(req,'login.html')

def cloud_logout(req):
    logout(req)
    return redirect(cloud_login)


# -----------------------------------------

def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        pswd=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,email=email,username=email,password=pswd)    
            data.save()
        except:
            messages.warning(req, "Username/email already exist.")
            return redirect(register)
        return redirect(cloud_login)
    else:
        return render(req,'register.html')
    



def upload(req):
    if req.method=='POST':
        files=req.FILES['file']
        data=Cloud.objects.create(all=files)
        data.save()
        return redirect(cloud_home)
    else:
            return render(req,'home.html')
    
    
def cloud_home(req):
    data=Cloud.objects.all()
    return render(req,'home.html',{'cloud':data})
