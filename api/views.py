import json
from urllib import response
from django.shortcuts import render
from fcm_django.models import FCMDevice
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, MultiPartParserError
from rest_framework_simplejwt.serializers import PasswordField
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, status, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from manageusers.models import Address
from categories.models import Category

# Create your views here.
class testapi(APIView):

    @staticmethod
    def get(request):
        data = [
            {
                "id": 1,
                "name": "fama0",
                "email": "fama1@gmail.com",
                "more": ['data1', 'data2'],
                "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
            },
            {
                "id": 2,
                "name": "fama1",
                "email": "fama1@gmail.com",
                "more": ['data1', 'data2'],
                "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"
            },

        ]
        res = {
            "status": Response.status_code,
            "message": str('fama, test api!'),
            "data": data
        }
        return Response(res)

from .serializers import RegisterSerializer,CustomTokenObtainPairSerializer,SalesAgentRegisterSerializer,CategorySerializer
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

# @csrf_exempt
# class LoginView(APIView):
#     # This view should be accessible also for unauthenticated users.
#     permission_classes = (permissions.AllowAny,)
#     @staticmethod
   
#     def post(self, request, format=None):
#         serializer = LoginSerializer(data=self.request.data,context={ 'request': self.request })
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return Response( status=status.HTTP_202_ACCEPTED)


# class ObtainJSONWebToken(TokenObtainPairView):
#     # Replace the serializer with your custom
#     serializer_class = CustomJWTSerializer
#     return response(CustomJWTSerializer.data)

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


####-----DealerRegistration-----####(coded by Prejin on 16-06-2022)
from rest_framework.parsers import MultiPartParser, FormParser

class DealerRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser)

    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {
            'user_type': request.data.get('user_type'),
            'username': request.data.get('name'),
            "shop_name":request.data.get('shop_name'),
            "gst_no":request.data.get('gst_no'),

            'email': request.data.get('username'),
            'mobile': request.data.get('phone'),
            'address': request.data.get('address'),
            'landmark': request.data.get('landmark'),
            'area': request.data.get('area'),
            'pincode': request.data.get('pincode'),



        }
        return Response(
            {'status_code': status.HTTP_201_CREATED, 'detail': 'You have successfully registered', 'data': data},
            status=status.HTTP_201_CREATED, headers=headers)

########--------SalesAgent Registerview ------------#######(coded by Prejin on 16-06-2022)
class SalesAgentRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser)

    serializer_class = SalesAgentRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {
            'user_type': request.data.get('user_type'),
            'username': request.data.get('username'),
            "shop_name":request.data.get('shop_name'),

            'email': request.data.get('email'),
            'mobile': request.data.get('phone'),
            'address': request.data.get('address'),
            'landmark': request.data.get('landmark'),
            'area': request.data.get('area'),
            'pincode': request.data.get('pincode'),



        }
        return Response(
            {"status_code": status.HTTP_201_CREATED, "detail":" You have successfully registered", "data": data},
            status=status.HTTP_201_CREATED, headers=headers)

#####----------CategoryView-----------###########
class GetCategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes=(AllowAny,)

    @staticmethod
    def get(request):
        # if Address.objects.filter(user_uuid=uuid).exists():
        crop_list=[]
        catarry=[]
        idarray=[]
        catelist=Category.objects.all()
        for cat in catelist:
            dictcat={}
            dictcat["category_id"]=cat.category_id
            dictcat["category_name"]=cat.category_name
            catarry.append(dictcat)
        dataset= {"status_code": "1", "message": "success", "data": catarry}
        return Response(dataset)
            #print(idarray)  