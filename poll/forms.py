from django.forms import ModelForm,Widget
from django import forms
from .models import polldata
from  datetime import datetime
class CreatePollform(forms.ModelForm):
    class Meta:
        model=polldata
        fields=["question","option_one","option_two","option_three","option_four","userid","time"]
        Widget={
            "question":forms.Textarea(attrs={'class':'form-control','rows':30})
        }
        


          
    