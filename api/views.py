import json
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

from .serializers import RegisterSerializer,LoginSerializer
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


@csrf_exempt
class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
        context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        password=serializer.validated_data['password']
        login(self,request, user)
        return Response( status=status.HTTP_202_ACCEPTED)


####-----DealerRegistration-----####
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
            'username': request.data.get('username'),
            'email': request.data.get('email'),
            'phone': request.data.get('phone'),
            'type': request.data.get('type'),
        }
        return Response(
            {'status_code': status.HTTP_201_CREATED, 'detail': 'You have successfully registered', 'data': data},
            status=status.HTTP_201_CREATED, headers=headers)

