from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    ACTIVE = 'active'
    INACTIVE = 'in-active'
    DELETED = 'delete'
    STATUS = [
        (ACTIVE, 'active'),
        (INACTIVE, 'in-active'),
        (DELETED, 'deleted'),
    ]
    DEALER = 'D'
    SALESAGENT = 'SA'
    TYPES = [
        (DEALER, 'Dealer'),
        (SALESAGENT, 'SalesAgent'),
    ]


    address_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    user_uuid=models.CharField(max_length=100,default='')
    name=models.CharField(max_length=150,unique=True,null=True)

    phone = models.CharField(max_length=70, default=None,null=True)
    email = models.EmailField(max_length=70, default=None,null=True)
    address = models.CharField(max_length=70, default=None,null=True)
    landmark = models.CharField(max_length=70, default=None,null=True)
    area = models.CharField(max_length=70, default=None,null=True)
    pincode = models.CharField(max_length=70, default=None,null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default=INACTIVE,
    )
    modified = models.DateTimeField(auto_now_add=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=10,choices=TYPES,default=DEALER)
   

class Dealers(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    ACTIVE = 'active'
    INACTIVE = 'in-active'
    DELETED = 'delete'
    STATUS = [
        (ACTIVE, 'active'),
        (INACTIVE, 'in-active'),
        (DELETED, 'deleted'),
    ]

    reg_dealer_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=150,unique=True,null=True)
    phone = models.CharField(max_length=70, default=None,null=True)
    email = models.EmailField(max_length=200)
    dealer_status=models.CharField(
        max_length=20,
        choices=STATUS,
        default=ACTIVE,
    )

    address_id=models.OneToOneField(Address,on_delete=models.CASCADE)
    dealer_image=models.ImageField(upload_to='dealer_images', blank=True, null=True)
    dealer_shopname=models.CharField(max_length=100,default=None,null=True)
    dealer_gst_no=models.CharField(max_length=200,default=None,null=True)
    
 ############################################################################   


# class SalesAddress(models.Model):

#     salesagent_address_id=models.AutoField(primary_key=True)
#     salesagent_city=models.CharField(max_length=150,unique=True,null=True)
#     salesagent_area=models.CharField(max_length=150,unique=True,null=True)
#     salesagent_country=models.CharField(max_length=150,unique=True,null=True)
#     salesagent_postalcode=models.CharField(max_length=150,unique=True,null=True)
  

# class SalesAgent(models.Model):
#     GENDER = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     )
#     ACTIVE = 'active'
#     INACTIVE = 'in-active'
#     DELETED = 'delete'
#     STATUS = [
#         (ACTIVE, 'active'),
#         (INACTIVE, 'in-active'),
#         (DELETED, 'deleted'),
#     ]

#     reg_salesagent_id = models.AutoField(primary_key=True)
#     salesagent_first_name=models.CharField(max_length=150,unique=True,null=True)
#     salesagent_last_name=models.CharField(max_length=150,unique=True,null=True)
#     salesagent_mobile_number=models.CharField(max_length=150,unique=True,null=True)
#     salesagent_gender=models.CharField(max_length=150,choices=GENDER)
#     salesagent_email = models.EmailField(max_length=200)
#     salesagent_status=models.CharField(
#         max_length=20,
#         choices=STATUS,
#         default=ACTIVE,
#     )

#     salesagent_address_id=models.ForeignKey(SalesAddress,related_name='saddress',on_delete=models.CASCADE)
#     salesagent_password=models.CharField(max_length=150,unique=True,null=True)
#     salesagent_confirm_password=models.CharField(max_length=150,unique=True,null=True)
    



