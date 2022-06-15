from . import views
from django.urls import path
# from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('addproduct', views.addproducts, name="addproduct"),
    # path('addproduct', views.addproducts.as_view(), name='addproduct'),
    path('listproduct', views.listproducts, name="listproduct"),
  
    path('editproduct/<int:pk>', views.editproducts.as_view(), name="editproduct"),
    path('deleteproduct/<int:pk>', views.deleteproducts.as_view(), name="deleteproduct"),
   
    
]