from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .uploadtoDb import uploadToDb
from .models import ImageUploader



# Create your views here.

def uploadPhoto(request):

    u=uploadToDb(request.POST,request.FILES)

    if request.method == 'POST':
        if u.is_valid():
            u.save()
            return redirect('upload')
        
        else :
            u=uploadToDb()

    return render(request,'phos/upload.html',{'u':u})



def getImage(request):

    image=ImageUploader.objects.all()

    return render(request,'phos/home.html',{'image':image})
