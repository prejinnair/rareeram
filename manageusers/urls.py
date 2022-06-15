from . import views
from django.urls import path
# from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', views.listdealers, name="listdealer"),
    # path('listsales', views.listSalesagents, name="listsalesagent"),
    # path('editdealer/<int:pk>', views.editedealers, name="editdealer"),
    # path('editdealer/<int:pk>', views.editedealers.as_view(), name="editdealer"),
    # path('editsales/<int:pk>', views.editsalesagent.as_view(), name="editsales"),


]