from . import views
from django.urls import path
# from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('modulesettings', views.modulesettings, name="modulesettings"),
    path('attribute', views.attribute, name="attribute"),
]