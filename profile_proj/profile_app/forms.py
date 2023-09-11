from django import forms 

class myform(forms.Form):
    name=forms.CharField()
    fathername=forms.CharField()
    mothername=forms.CharField()
    Email=forms.EmailField()
    roll_no=forms.IntegerField()
    stream=forms.CharField()
    address=forms.CharField()
    state=forms.CharField()
    city=forms.CharField()
    pin_code=forms.CharField()
    gender=forms.CharField()
    mobile_no=forms.IntegerField()
    image=forms.ImageField()
    description=forms.CharField()