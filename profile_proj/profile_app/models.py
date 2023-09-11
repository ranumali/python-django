from django.db import models

# Create your models here.

class myprofile(models.Model):
    name=models.CharField(max_length=50)
    fathername=models.CharField(max_length=50)
    mothername=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    roll_no=models.IntegerField()
    stream=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pin_code=models.CharField(max_length=6)
    gender=models.CharField(max_length=50)
    mobile_no=models.IntegerField()
    image=models.ImageField(upload_to='media',null=True)
    description=models.CharField(max_length=400)
    
    