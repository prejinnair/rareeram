from django.shortcuts import render,redirect
from django.views import View

from categories.models import Category

# from Rareeram.categories.models import Category

# from Rareeram.categories import views

# Create your views here.

from . models import Products
from products.forms import ProductForm
import os
# from django.utils import getFormData
import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


def addproducts(request):
    product_form = ProductForm(request.POST or None,request.FILES)
    if product_form.is_valid():
            product = Products()
            data=request.POST
            color=data["color"]
            size=data["size"]
            price=data["price"]
            price2=data["price2"]

            split = os.path.splitext(str(request.FILES['product_image']))

            product_form.save()

            product_last= Products.objects.last()
            product_did=product_last.product_id
            update = Products.objects.filter(product_id=product_did).update(product_attributes={"color":color,"size":size,"price":price,"price2":price2})
                
            return redirect("listproduct")
    else:
        return render(request, "Products/addproduct.html", {"product_form": product_form})
                





# class addproducts(View):

#     @staticmethod
#     def post(request):
#         form = ProductForm(request.POST,request.FILES)
#         if form.is_valid():
#             prod = Products()
           
#             split = os.path.splitext(str(request.FILES['product_image']))
            
#             prod.product_image =request.FILES['product_image']
#             prod.product_name=getFormData(request,'product_name')
#             prod.product_descriptions=getFormData(request,'product_descriptions')
#             # prod.product_image=getFormData(request,'product_image')
#             prod.category_id = Category.objects.get(category_id=getFormData(request, 'category_id'))
#             prod.save()
#             form = ProductForm()
#             messages.success(request, 'added success')
   
#         # 
        
#         context = {'form': form}
#         return render(request, "Products/addproduct.html", context)

#     @staticmethod
#     def get(request):
#         form = ProductForm()
#         context = {'form': form}
#         return render(request, "Products/addproduct.html", context)


def listproducts(request):
    products= Products.objects.all()
    print(products)
    return render(request,"Products/listproduct.html",{'products': products})

    
# class editproducts(View):
    
#     print("edi1sdfghj")

#     @staticmethod
#     def get(request, pk):
#         products = Products.objects.get(product_id=pk)

        
        
#         product_form = ProductForm(initial={'product_name': products.product_name,
#                                             'product_attributes': products.product_attributes,
#                                             'product_descriptions': products.product_descriptions,
#                                             'category_id':products.category_id,
#                                             'product_image':products.product_image

#                                                                             })
#         print(product_form,"haii")
#         #p_props=eval(products.product_attributes)
#         p_props=eval(products.product_attributes)
        
#         # print(p_props)
#         color=p_props["color"]
#         size=p_props["size"]
#         price=p_props["price"]
#         price2=p_props["price2"]

#         context = {'product_form': product_form, 'products': products, 'pk': pk,"color":color,"size":size,"price":price,"price2":price2}
#         # print(context,"dgfhgjkl;lsrtdrhtfjgykhljsadfghjk1111111111111111111111111")
#         return render(request, 'Products/editproduct.html', context)
   
    # @staticmethod
    # def post(request,pk):
        
    #     # if len(request.FILES) != 0:

    #         # data = request.FILES['some_file']
    # # ...do some work...
    #     # else:
    #     # return redirect('/nofile/' {'foo': bar})
        
    #     print("helooooooooooooooooooooooooooo")
       
    #     product_form = ProductForm(request.POST,request.FILES)
        
        
    #     if product_form.is_valid():
            

    #         split = os.path.splitext(str(product_form.cleaned_data['product_image']))
    #         # print(request.FILES['product_image'])
            
    #         print(request.FILES['product_image'].name)
       

        
    #     Products.objects.filter(pk=pk).update(product_name=request.POST.get('product_name'),
    #                                             product_attributes=request.POST.get('product_attributes'),
    #                                             product_descriptions=request.POST.get('product_descriptions'),
    #                                             # product_image=request.POST.get('product_image'),
    #                                             category_id=request.POST.get('category_id'),
    #                                             # product_image=request.FILES['product_image']

    #         )

        
                

    #     Prodobj = get_object_or_404(Products, pk=pk)
    #     Prodobj.product_image = request.FILES['product_image']
    #     print(Prodobj,"22222222222222222222222233333")
    #     Prodobj.save()
        
    #     data=request.POST
    #     print(data)
    #     color=data["color"]
    #     size=data["size"]
    #     price=data["price"]
    #     price2=data["price2"]
    #     product_last= Products.objects.last()
    #     product_did=product_last.product_id
    #     update = Products.objects.filter(pk=pk).update(product_attributes={"color":color,"size":size,"price":price,"price2":price2})
        
        


    #     messages.success(request, f'Products with id({pk}) is updated successfully')
    #     return redirect("/listproduct",pk=pk)
    #     return redirect("listproduct",pk=pk)
######################################################### main #####################################################   

################################# rough#########################
class editproducts(View):
    
    print("edi1sdfghj")

    @staticmethod
    def get(request, pk):
        products = Products.objects.get(product_id=pk)

        
        
        product_form = ProductForm(initial={'product_name': products.product_name,
                                            'product_attributes': products.product_attributes,
                                            'product_descriptions': products.product_descriptions,
                                            'category_id':products.category_id,
                                            'product_image':products.product_image

                                                                            })
        print(product_form,"haii")
        #p_props=eval(products.product_attributes)
        p_props=eval(products.product_attributes)
        
        # print(p_props)
        color=p_props["color"]
        size=p_props["size"]
        price=p_props["price"]
        price2=p_props["price2"]

        context = {'product_form': product_form, 'products': products, 'pk': pk,"color":color,"size":size,"price":price,"price2":price2}
        # print(context,"dgfhgjkl;lsrtdrhtfjgykhljsadfghjk1111111111111111111111111")
        return render(request, 'Products/editproduct.html', context)
   

    @staticmethod
    def post(request,pk):
        
        
        
        print("helooooooooooooooooooooooooooo")
       
        #product_form = ProductForm(request.POST,request.FILES)
       # product_form = ProductForm(request.POST)
        #if product_form.is_valid():
          
        #split = os.path.splitext(str(product_form.cleaned_data['product_image']))
                # print(request.FILES['product_image'])
            
        #print(request.FILES['product_image'])
        


        Products.objects.filter(pk=pk).update(product_name=request.POST['product_name'],
                                                # product_attributes=request.POST['product_attributes'],
                                                product_descriptions=request.POST['product_descriptions'],
                                                # product_image=request.POST.get('product_image'),
                                                category_id=request.POST['category_id'],
                                                # product_image=request.FILES['product_image']
                                                )
        # print(Products,"formss update checking###########&&&&&&&&&&")

            
        if len(request.FILES) != 0:
            Prodobj = get_object_or_404(Products, pk=pk)
            print("request")
            Prodobj.product_image = request.FILES['product_image']
            print(Prodobj,"22222222222222222222222233333")
            Prodobj.save()
        
        data=request.POST
        print("dtas",data)
        color=data["color"]
        size=data["size"]
        price=data["price"]
        price2=data["price2"]
        product_last= Products.objects.last()
        product_did=product_last.product_id
        update = Products.objects.filter(pk=pk).update(product_attributes={"color":color,"size":size,"price":price,"price2":price2})
        # return redirect("/listproduct",pk=pk)
        
        messages.success(request, f'Products with id({pk}) is updated successfully')
        return redirect("listproduct")
            
        return redirect("listproduct")
    
 ##################################################################










    

class deleteproducts(View):
    @staticmethod
    def get(request, pk):
        products= Products.objects.get(product_id=pk)
        products.delete()
        print("deleted")
        return redirect("listproduct")




#######################################3#######################################33


