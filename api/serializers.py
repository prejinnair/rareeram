from datetime import datetime
import email
from pyexpat import model
from urllib import response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import uuid 
import json
from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.serializers import Serializer, FileField, ImageField
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from Rareeram import settings
from manageusers.models import Dealers,Address
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from django.contrib.auth import authenticate, get_user_model
from rest_framework_jwt.settings import api_settings


def create_UUID():

	return uuid.uuid4()

# class LoginSerializer(serializers.Serializer):
#     """
#     This serializer defines two fields for authentication:
#       * username
#       * password.
#     It will try to authenticate the user with when validated.
#     """
#     username = serializers.CharField(
#         label="Username",
#         write_only=True
#     )
#     password = serializers.CharField(
#         label="Password",
#         # This will be used when the DRF browsable API is enabled
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#         write_only=True
#     )
#     print(username)

#     def validate(self, attrs):
#         # Take username and password from request
#         username = attrs.get('username')
#         password = attrs.get('password')

#         if username and password:
#             # Try to authenticate the user using Django auth framework.
#             user = authenticate(request=self.context.get('request'),
#                                 username=username, password=password)
#             if not user:
#                 # If we don't have a regular user, raise a ValidationError
#                 msg = 'Access denied: wrong username or password.'
#                 raise serializers.ValidationError(msg, code='authorization')
#         else:
#             msg = 'Both "username" and "password" are required.'
#             raise serializers.ValidationError(msg, code='authorization')
#         # We have a valid user, put it in the serializer's validated_data.
#         # It will be used in the view.
#         attrs['user'] = user
#         return attrs
#################------------login------------##########
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include

        if User.objects.filter(id=self.user.id).exists():
            user_data = User.objects.get(id=self.user.id)
            ad_obj=Address.objects.get(user_id=self.user.id)
            uuid=ad_obj.user_uuid
            phone=ad_obj.phone


            




        else:
            print("none")
            user_type = None

        data.update({'id': self.user.id,"username":self.user.username,"uuid":uuid,"phone":phone})
        # data.update({'user_type': user_type})
        # and everything else you want to send in the response
        return data



User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

# class CustomJWTSerializer(JSONWebTokenSerializer):
#     username_field = 'username_or_email'

#     def validate(self, attrs):

#         password = attrs.get("password")
#         user_obj = User.objects.filter(email=attrs.get("username_or_email")).first() or User.objects.filter(username=attrs.get("username_or_email")).first()
#         if user_obj is not None:
#             credentials = {
#                 'username':user_obj.username,
#                 'password': password
#             }
#             if all(credentials.values()):
#                 user = authenticate(**credentials)
#                 if user:
#                     if not user.is_active:
#                         msg = _('User account is disabled.')
#                         raise serializers.ValidationError(msg)

#                     payload = jwt_payload_handler(user)

#                     return {
#                         'token': jwt_encode_handler(payload),
#                         'user': user
#                     }
#                 else:
#                     msg = _('Unable to log in with provided credentials.')
#                     raise serializers.ValidationError(msg)

#             else:
#                 msg = _('Must include "{username_field}" and "password".')
#                 msg = msg.format(username_field=self.username_field)
#                 raise serializers.ValidationError(msg)

#         else:
#             msg = _('Account with this email/username does not exists')
#             raise serializers.ValidationError(msg)

#         return response(attrs)
# from rest_framework_simplejwt.serializers import TokenObtainSerializer


# class EmailTokenObtainSerializer(TokenObtainSerializer):
#     username_field = User.EMAIL_FIELD


# class CustomTokenObtainPairSerializer(EmailTokenObtainSerializer):
#     @classmethod
#     def get_token(cls, user):
#         return RefreshToken.for_user(user)

#     def validate(self, attrs):
#         data = super().validate(attrs)

#         refresh = self.get_token(self.user)

#         data["refresh"] = str(refresh)
#         data["access"] = str(refresh.access_token)

#         return data


######-------------DealerRegister Serializer--------------###3

class RegisterSerializer(serializers.ModelSerializer):
   
   
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmpassword = serializers.CharField(write_only=True, required=True)
    user_type = serializers.CharField(write_only=True, required=True)
    name= address = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(write_only=True,
                                  validators=[UniqueValidator(queryset=Dealers.objects.all()),
                                              
                                              ], required=True)
    dealer_image = serializers.ImageField(required=False)                                         
    address = serializers.CharField(write_only=True, required=True)
    landmark = serializers.CharField(write_only=True, required=True)
    area = serializers.CharField(write_only=True, required=True)
    pincode = serializers.CharField(write_only=True, required=True)
    shop_name=serializers.CharField(write_only=True, required=True)
    gst_no=serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        exclude = ['last_name']
        # fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True}
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirmpassword']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
           
            first_name=validated_data['name'],
            username=validated_data['username'],
            email=validated_data['username'],
            is_active=True
        )

        address = Address()
        address.user_id = user
        # address.name = user.username
        # address.lastname = user
        address.phone = validated_data['phone']
        address.email = user.username
        address.status = 'a'
        address.address = validated_data.pop('address')
        address.landmark = validated_data.pop('landmark')
        address.area = validated_data.pop('area')
        address.pincode = validated_data.pop('pincode')
        address.type=validated_data.pop('user_type')
        address.user_uuid=create_UUID()
    

        address.save()

        user.set_password(validated_data['password'])

      
        employee = Dealers()
        employee.address_id = address
        employee.user_id = user
        employee.phone = validated_data.pop('phone')
        employee.address_id = address
        employee.dealer_shopname=validated_data.pop('shop_name')
        employee.dealer_gst_no=validated_data.pop('gst_no')
        employee.email=user.username
        # employee.dealer_image=validated_data.pop('dealer_image')
        user.save()
        employee.save()

 

        return user
    