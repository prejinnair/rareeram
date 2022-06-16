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
from manageusers.models import Dealers,Address,SalesAgent
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from categories.models import Category
from django.contrib.auth import authenticate, get_user_model
from rest_framework_jwt.settings import api_settings


def create_UUID():

	return uuid.uuid4()


#################------------login------------##########(coded by Prejin on 15-06-2022)
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

        data.update({'id': self.user.id,"username":self.user.first_name,"uuid":uuid,"phone":phone,"email":self.user.username,"user_type":ad_obj.type,
        "created_at":ad_obj.entry_date,"updated_at":ad_obj.modified,"last_login_at":"","last_login_ip":"","created_user":"","updated_user":'',"is_removable:":'',"is_admin":self.user.is_superuser,"password_reset_link":""})
        dataset = {"status": "1","message": "Login Successfull","data":data}
        # data.update({'user_type': user_type})
        # and everything else you want to send in the response
        return dataset



User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER



######-------------DealerRegister Serializer--------------###(coded by Prejin on 15-06-2022)

class RegisterSerializer(serializers.ModelSerializer):
   
   
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmpassword = serializers.CharField(write_only=True, required=True)
    user_type = serializers.CharField(write_only=True, required=True)
    name=serializers.CharField(write_only=True, required=True)
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
        address.name = user.first_name
        # address.lastname = user
        address.phone = validated_data['phone']
        address.email = user.username
        address.status = 'active'
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
        employee.name = user.first_name
        employee.phone = validated_data.pop('phone')
        employee.address_id = address
        employee.dealer_shopname=validated_data.pop('shop_name')
        employee.dealer_gst_no=validated_data.pop('gst_no')
        employee.email=user.username
        employee.status="in-active"
        # employee.dealer_image=validated_data.pop('dealer_image')
        user.save()
        employee.save()

 

        return user
    
##############-------SalesAgent Register Serializer--------#############(coded by Prejin on 16-06-2022)
class SalesAgentRegisterSerializer(serializers.ModelSerializer):
   
   
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmpassword = serializers.CharField(write_only=True, required=True)
    user_type = serializers.CharField(write_only=True, required=True)
    name=serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(write_only=True,
                                  validators=[UniqueValidator(queryset=SalesAgent.objects.all()),
                                              
                                              ], required=True)
    salesagent_image = serializers.ImageField(required=False)                                         
    # address = serializers.CharField(write_only=True, required=True)
    # landmark = serializers.CharField(write_only=True, required=True)
    # area = serializers.CharField(write_only=True, required=True)
    # pincode = serializers.CharField(write_only=True, required=True)
    # shop_name=serializers.CharField(write_only=True, required=True)
    # gst_no=serializers.CharField(write_only=True, required=True)

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
        address.name = user.first_name
        # address.lastname = user
        address.phone = validated_data['phone']
        address.email = user.username
        address.status = 'active'
        # address.address = validated_data.pop('address')
        # address.landmark = validated_data.pop('landmark')
        # address.area = validated_data.pop('area')
        # address.pincode = validated_data.pop('pincode')
        address.type=validated_data.pop('user_type')
        address.user_uuid=create_UUID()
    

        address.save()

        user.set_password(validated_data['password'])

      
        employee = SalesAgent()
        employee.address_id = address
        employee.name = user.first_name
        employee.user_id = user
        employee.phone = validated_data.pop('phone')
        employee.email=user.username
        employee.status="in-active"
        # employee.dealer_image=validated_data.pop('dealer_image')
        user.save()
        employee.save()

 

        return user
#####@#-------------------getcategory-----------######

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'