from django.db import models

from categories.models import *
# Create your models here.

class Products(models.Model):

    product_id = models.AutoField(primary_key=True,unique=True)
    product_name =models.CharField(max_length=150,unique=True,null=True)
    category_id=models.ForeignKey(Category ,related_name='category',on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to = 'images/', blank=True,null=True)
    product_attributes=models.TextField("Item Details JSON" ,null=True)
    product_descriptions=models.TextField(max_length=300,unique=True,null=True)

    def __str__(self):
        return '{}'.format(self.product_name)

    # def _str_(self):
    #     return str(self.category_id.category_name)