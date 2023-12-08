from django import forms
from phos.models import ImageUploader
from .models import UserProfile

class Userdetails(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['profile_pic','name','bio']
        labels={'profile_pic':'','name':'','bio':''}
        