from .models import Image, Comments, Followers, Profile
from django import forms
from django.forms import ModelForm, Textarea, IntegerField

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'userId', 'user']