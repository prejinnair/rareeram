from django.shortcuts import render

# Create your views here.
def modulesettings(request):
    return render(request,"module/modulesettings.html")

def attribute(request):
    return render(request,"module/attribute.html")
