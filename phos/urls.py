from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('upload/',views.uploadPhoto,name='upload'),
    path('',views.getImage,name='home'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
