from django import forms
from .models import ImageUploader

class uploadToDb(forms.ModelForm):
    class Meta:
        model=ImageUploader
        fields=('photo',)
        labels={'photo':''}
