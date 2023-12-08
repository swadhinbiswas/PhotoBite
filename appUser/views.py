from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from .models import UserProfile

@login_required(login_url='signin')
def Dashbord(request):
    return render(request,'appUser/dashbord.html')

# Create your views here.
def  LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('dashbord')
        else:
            messages.error(request,'invalid credentials')
            




    return render(request,'appUser/login.html')

def SignUp(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2 =request.POST.get('password2')


        if password1!=password2:

            messages.error(request,'password do not match')
            
        else:
            appuser=User.objects.create_user(username,email,password1)
            appuser.save()
            messages.success(request,'User Created Successfully')

            return redirect ('signin')
            
             


    return render(request,'appUser/signup.html')


def Signout(request):

    return render(request,'appUser/logout.html')


#def getUsername(request):
   # username=request.user
  #  return render(request,'appUser/dashbord.html',{'username':username})


@login_required(login_url='signin')
def userInfo(request):

    if request.method=='POST':
        name=request.POST.get('name')
        bio=request.POST.get('bio')
        profile_pic=request.FILES.get('profilePicture')
        user=request.user
        userprofile=UserProfile(user=user,name=name,bio=bio,profile_pic=profile_pic)
        userprofile.save()

        redirect(request,'dashbord')
    return render(request,'appUser/userinfo.html')