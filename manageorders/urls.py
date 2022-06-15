from . import views
from django.urls import path


urlpatterns = [

    path('addorder', views.addorders, name="addorder"),
    path('listorder', views.listorders, name="listorder"),
]