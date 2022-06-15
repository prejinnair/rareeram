from django.shortcuts import render
# from Rareeram.manageusers.models import SalesAgent
# from Rareeram.manageusers.models import Address,Dealers

# Create your views here.
from .models import Dealers,Address
import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
# from .forms import DealerForm,AddressForm,AgentAddressForm,SaleAgentForm
# ,AgentAddressForm,SaleAgentForm

from django.views import View
# from .models import Dealers
# class editedealers(View):
#     def __init__(self):
#         self.dealerform=DealerForm()
#         self.addressform=AddressForm()

#         self.context={"dealerform":self.dealerform,'addressform':self.addressform}
#     def get(self,request,pk):

#         dealers=Dealers.objects.get(reg_dealer_id=pk)
#         address=Address.objects.get(address_id=pk)

#         if address.address_id is not None and Address.objects.filter(address_id=address.address_id).exists():
#             address = Address.objects.get( address_id=address.address_id)

#             self.dealerform=DealerForm(initial={"reg_dealer_id":dealers.reg_dealer_id,
#                                         "dealer_first_name":dealers.dealer_first_name,
#                                         "dealer_last_name":dealers.dealer_last_name,
#                                         "dealer_mobile_number":dealers.dealer_mobile_number,
#                                         "dealer_gender":dealers.dealer_gender,
#                                         "dealer_status":dealers.dealer_status,




#             })

#             self.addressform=AddressForm(initial={"address_id":address.address_id,
#                                         "city":address.city,
#                                         "area":address.area,
#                                         "country":address.country,
#                                         "postalcode":address.postalcode,
                                       
#             })
#             self.context = {'dealerform':self.dealerform,'addressform':self.addressform,"pk":pk}
#             return render(request,"ManageUsers/editdealer.html",self.context)

#         # def post(self,request,pk):


#     def post(self, request, pk):

#         # getting updated form data
#         self.dealerform = DealerForm(request.POST)
#         self.addressform = AddressForm(request.POST)

#         if self.dealerform.is_valid():

           
       
       
#             Dealers.objects.filter(reg_dealer_id=pk).update(
#                 dealer_first_name=request.POST.get('dealer_first_name'),
#                 dealer_last_name=request.POST.get('dealer_last_name'),
#                 dealer_mobile_number=request.POST.get('dealer_mobile_number'),
#                 dealer_gender=request.POST.get('dealer_gender'),
#                 dealer_status=request.POST.get('dealer_status'),
                

#             )
            

#             # # updating address table
#             Address.objects.filter(address_id=pk).update(
#                 city=request.POST.get('city'),
#                 area=request.POST.get('area'),
#                 country=request.POST.get('country'),
#                 postalcode=request.POST.get('postalcode'),
               

#             )
#             dealerobj = get_object_or_404(Address, pk=pk)
            
#             dealerobj.save()
#             messages.success(
#                 request, f'Dealers with id({pk}) is updated successfully')
#             return redirect('listdealer', pk=pk)

#         else:
#             self.context = {'addressform': self.addressform,
#                             'dealerform': self.dealerform, 'pk': pk}
#             return render(request, 'ManageUsers/editdealer.html', self.context)





def listdealers(request):
    dealers=Dealers.objects.all()

    return render(request,"ManageUsers/listdealer.html",{'dealers':dealers})
#####################################################################################


# class editsalesagent(View):
#     def __init__(self):
#         self.salesform=SaleAgentForm()
#         self.salesaddressform=AgentAddressForm()

#         self.context={"salesform":self.salesform,'salesaddressform':self.salesaddressform}
#     def get(self,request,pk):

#         salesagent=SalesAgent.objects.get(reg_salesagent_id=pk)
#         salesaddress=SalesAddress.objects.get(salesagent_address_id=pk)

#         if salesaddress.salesagent_address_id is not None and SalesAddress.objects.filter(salesagent_address_id=salesaddress.salesagent_address_id).exists():
#             salesaddress = SalesAddress.objects.get( salesagent_address_id=salesaddress.salesagent_address_id)

#             self.salesform=SaleAgentForm(initial={"reg_salesagent_id":salesagent.reg_salesagent_id,
#                                         "salesagent_first_name":salesagent.salesagent_first_name,
#                                         "salesagent_last_name":salesagent.salesagent_last_name,
#                                         "salesagent_mobile_number":salesagent.salesagent_mobile_number,
#                                         "salesagent_gender":salesagent.salesagent_gender,
#                                         "salesagent_status":salesagent.salesagent_status,




#             })

#             self.salesaddressform=AgentAddressForm(initial={"salesagent_address_id":salesaddress.salesagent_address_id,
#                                         "salesagent_city":salesaddress.salesagent_city,
#                                         "salesagent_area":salesaddress.salesagent_area,
#                                         "salesagent_country":salesaddress.salesagent_country,
#                                         "salesagent_postalcode":salesaddress.salesagent_postalcode,
                                       
#             })
#             self.context = {'salesform':self.salesform,'salesaddressform':self.salesaddressform,"pk":pk}
#             return render(request,"ManageUsers/editsales.html",self.context)

        # def post(self,request,pk):


    # def post(self, request, pk):

    #     # getting updated form data
    #     self.salesform = SaleAgentForm(request.POST)
    #     self.salesaddressform = AgentAddressForm(request.POST)

    #     if self.salesform.is_valid():

    #         SalesAddress.objects.filter(reg_salesagent_id=pk).update(
    #             salesagent_first_name=request.POST.get('salesagent_first_name'),
    #             salesagent_last_name=request.POST.get('salesagent_last_name'),
    #             salesagent_mobile_number=request.POST.get('salesagent_mobile_number'),
    #             salesagent_gender=request.POST.get('salesagent_gender'),
    #             salesagent_status=request.POST.get('salesagent_status'),
            
    #         )
           
    #         # # updating address table
    #         SalesAddress.objects.filter(salesagent_address_id=pk).update(
    #             salesagent_city=request.POST.get('salesagent_city'),
    #             salesagent_area=request.POST.get('salesagent_area'),
    #             salesagent_country=request.POST.get('salesagent_country'),
    #             salesagent_postalcode=request.POST.get('salesagent_postalcode'),
               

    #         )
    #         salesrobj = get_object_or_404(SalesAddress, pk=pk)
            
    #         salesrobj.save()
    #         messages.success(
    #             request, f'salesagent with id({pk}) is updated successfully')
    #         return redirect('listsales', pk=pk)

    #     else:
    #         self.context = {'salesaddressform': self.salesaddressform,
    #                         'salesform': self.salesform, 'pk': pk}
    #         return render(request, 'ManageUsers/editsales.html', self.context)



# def listSalesagents(request):
#     salesagents=SalesAgent.objects.all()

#     return render(request,"ManageUsers/listsales.html",{'salesagents':salesagents})
