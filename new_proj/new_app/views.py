from django.shortcuts import render

# Create your views here.

def input(request):
    return render(request,'index.html')

def  dum(request):
    return render(request,'product.html')
def dim(request):
    return render(request,'display.html')
def desh(request):
    return render(request,'contect.html')
