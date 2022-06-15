from . import views
from django.urls import path
# from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('rolepermission', views.rolepermission, name="rolepermission"),
    path('role', views.role, name="role"),
    path('success', views.success, name="success"),
    path('users', views.users, name="users"),
    path('update', views.update, name="update"),
]