from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import UserProfile

# Create your views here.
def rolepermission(request):
    return render(request,"Role/rolepermission.html")

def role(request):
    return render(request,"Role/role.html")

def success(request):
    return render(request,"Role/success.html")

def update(request):
    return render(request,"Role/update.html")

def users(request):
    if request.method=="POST":
        firstname=request.POST.get("userprofile_firstname")
        lastname=request.POST.get("userprofile_lastname")
        username=request.POST.get("userprofile_username")
        email=request.POST.get("userprofile_email")
        dob=request.POST.get("userprofile_dob")
        phone=request.POST.get("userprofile_phoneno")
        password=request.POST.get("userprofile_password")
        conpassword=request.POST.get("userprofile_conpassword")
        
        
        obj = UserProfile.objects.create(userprofile_firstname=firstname,userprofile_lastname=lastname,
        userprofile_username=username,userprofile_email=email,userprofile_dob=dob,userprofile_phoneno=phone,
        userprofile_password=password,userprofile_conpassword=conpassword)
        obj = UserProfile(userprofile_firstname=firstname,userprofile_lastname=lastname,
        userprofile_username=username,userprofile_email=email,userprofile_dob=dob,userprofile_phoneno=phone,
        userprofile_password=password,userprofile_conpassword=conpassword)
        
        obj.save()
        #return render(request,'index.html',{'obj':obj})
        # return redirect('/')
    return render(request,"Role/users.html")

