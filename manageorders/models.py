from django.db import models
# Create your models here.

class Orders(models.Model):

    ACTIVE = 'active'
    INACTIVE = 'in-active'
    DELETED = 'delete'

    STATUS = [
        (ACTIVE, 'active'),
        (INACTIVE, 'in-active'),
        (DELETED, 'deleted'),
    ]

    order_id = models.AutoField(primary_key=True)
    order_name=models.CharField(max_length=150,unique=True,null=True)
    order_date=models.CharField(max_length=70)
    order_status=models.CharField(
        max_length=20,
        choices=STATUS,
        default=ACTIVE,
    )
    order_email=models.EmailField(max_length=200)
    order_decription=models.CharField(max_length=70)
    order_phone=models.CharField(max_length=150,unique=True,null=True)
    order_tracking_no=models.CharField(max_length=70)
    order_shipping_provider=models.CharField(max_length=100)
    order_date_shipped=models.DateField(auto_now_add=True)
    order_total=models.CharField(max_length=300)
    
    
