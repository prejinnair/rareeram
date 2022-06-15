from django.shortcuts import render
from .models import Orders
from django.shortcuts import render
# from Rareeram.manageusers.models import SalesAgent
# from Rareeram.manageusers.models import Address,Dealers

# Create your views here.
from .models import Orders
import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
# Create your views here.

def listorders(request):
    orders=Orders.objects.all()

    return render(request,"ManageOrders/listorders.html",{'orders':orders})


def addorders(request):

    order_form = OrderForm(request.POST)
    if order_form.is_valid():
        order_form.save()
        

        return redirect("listorders")
    else:
        return render(request, "ManageOrders/add.html", {"order_form": order_form})
   