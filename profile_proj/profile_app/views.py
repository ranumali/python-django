from django.shortcuts import render,HttpResponse
from .models import myprofile
from .forms import myform


# Create your views here.

def profile(request):
    if request.method=="POST":
        name = request.POST['name']
        fathername = request.POST['fathername']
        mothername = request.POST['mothername']
        Email = request.POST['Email'] 
        roll_no = request.POST['roll_no']
        stream = request.POST['stream']  
        city = request.POST['city']   
        state = request.POST['state']
        gender = request.POST['gender']
        pin_code = request.POST['pin_code'] 
        image  = request.POST['image'] 
        description = request.POST['description']
        address = request.POST['address']
        mobile_no = request.POST['mobile_no']
        myprofile(name=name,fathername=fathername,mothername=mothername,Email=Email,roll_no=roll_no, stream=stream,city=city,state=state,gender=gender,pin_code=pin_code,image=image,description=description,address=address,mobile_no=mobile_no).save()
       
        print(name,fathername,mothername,Email,roll_no,stream,city,state,gender,pin_code,image,description,address,mobile_no)
   
    return render(request,'profile.html')
def myforms(request):
   if request.method=="POST":
       a=myform(request.POST,request.FILES)
       print(a)
       
       if a.is_valid():
        name =a. cleaned_data['name']
        fathername =a.cleaned_data['fathername']
        mothername =a.cleaned_data['mothername']
        Email = a.cleaned_data['Email'] 
        roll_no =a.cleaned_data['roll_no']
        stream = a.cleaned_data['stream']  
        city = a.cleaned_data['city']   
        state = a.cleaned_data['state']
        gender = a.cleaned_data['gender']
        pin_code = a.cleaned_data['pin_code'] 
        image  = a.cleaned_data['image'] 
        description =a. cleaned_data['description']
        address =a.cleaned_data['address']
        mobile_no = a.cleaned_data['mobile_no']
        myprofile(name=name,fathername=fathername,mothername=mothername,Email=Email,roll_no=roll_no, stream=stream,city=city,state=state,gender=gender,pin_code=pin_code,image=image,description=description,address=address,mobile_no=mobile_no).save()
        return HttpResponse('Data saved !!!')

   a=myform()
   context={
    
       'a':a
   }
   return render(request,'forms.html',context)

def get_data(request):
   data = myprofile.objects.all()
   print(data)