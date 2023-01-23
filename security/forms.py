from django import forms
from django.forms import ModelForm,Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class userregistrationform(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    bio=forms.CharField(max_length=100)
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password1","password2","bio"]