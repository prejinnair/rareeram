from . import views
from django.urls import path


urlpatterns = [
    path('login/', views.login.as_view(), name="login"),
    path('logout/', views.logout, name="logout")
]