from datetime import datetime
from pyexpat import model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import uuid 

from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.serializers import Serializer, FileField, ImageField
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

from Rareeram import settings
from manageusers.models import Dealers,Address
# from announcement.models import AnnouncementModel
# from api.models import CropType, DiseaseType, FarmType
# from block.models import Block
# from college.models import College, Department
# from district.models import District
# from employee.models import KrishiBhavanEmployee, Address, Scientist, Farmer
# from krishi_office.models import KrishiBhavan
# from ticket.models import Ticket, UploadImage, FollowUp
# from util import generateToken
# from zone.models import Zone
# from POP.models import Category,CropItem,Update
# from gallery.models import *

def create_UUID():

	return uuid.uuid4()

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        attrs['password']=password
        return attrs

######-------------DealerRegister Serializer--------------###3

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmpassword = serializers.CharField(write_only=True, required=True)
    type = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(write_only=True,
                                  validators=[UniqueValidator(queryset=Dealers.objects.all()),
                                              
                                              ], required=True)
    dealer_image = serializers.ImageField(required=False)                                         
    address = serializers.CharField(write_only=True, required=True)
    landmark = serializers.CharField(write_only=True, required=True)
    area = serializers.CharField(write_only=True, required=True)
    pincode = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        exclude = ['first_name','last_name']
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
           
            username=validated_data['username'],
            email=validated_data['email'],
            # last_name=validated_data['last_name'],
            is_active=True
        )

        address = Address()
        address.user_id = user
        address.name = user.username
        # address.lastname = user
        address.phone = validated_data['phone']
        address.email = user.email
        address.status = 'a'
        address.address = validated_data.pop('address')
        address.landmark = validated_data.pop('landmark')
        address.area = validated_data.pop('area')
        address.pincode = validated_data.pop('pincode')
        address.type=validated_data.pop('type')
        address.user_uuid=create_UUID()
    

        address.save()

        user.set_password(validated_data['password'])

      
        employee = Dealers()
        employee.address_id = address
        employee.user_id = user
        employee.phone = validated_data.pop('phone')
        employee.address_id = address
        employee.dealer_image=validated_data.pop('dealer_image')
        user.save()
        employee.save()

 

        return user