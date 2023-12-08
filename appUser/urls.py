from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from phos.views import getImage

urlpatterns = [
    path('signin/',views.LoginPage,name='signin'),
    path('signup/',views.SignUp,name='signup'),
    path('dashbord/',views.Dashbord,name='dashbord'),
    path('logout/',getImage,name='logout'),
    path('userinfo/',views.userInfo,name='userinfo'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)