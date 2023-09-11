from django.shortcuts import render

# Create your views here.
def indext(request):
    return render(request,'index.html')