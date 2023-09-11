from django.shortcuts import render,HttpResponse
from .models import student_details
from .forms import myform
from .forms import student,form_data,student_form

# Create your views here.
def index(request):
    data = student_details.objects.all()

    context= {
        'd':data
    }
    
    return render(request,'index.html',context)




def forms(request):
    if request.method=="POST":
        a=myform(request.POST)
   if a.is_valid():
       

        n=request.POST['name']
        e=request.POST['email']
        form_data(name=n,email=e,address=a).save()
        return HttpResponse("your data saved!!!")
    else:
        return HttpResponse("data not saved!!!")
    else:
        
        a=myform()
        print(a)
        context={
            'a':a
        }
        
        return render(request,'form.html',context)


