from django import forms
from .models import student_details

class myform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField()
    pin_code=forms.IntegerField()
    
