from django.db import models

# Create your models here.
class student_details(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=100)
    state=models.CharField(max_length=20)   
    city=models.CharField(max_length=20)
    pin_code=models.IntegerField()
  
  
    class form_data(models.Model):
    name =models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=20)
        