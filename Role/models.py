from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# from django_countries.fields import CountryField
# Create your models here.
class UserProfile(models.Model):
	
	userprofile_firstname=models.CharField(max_length=100,default='')
	userprofile_lastname=models.CharField(max_length=100,default='')
	userprofile_username=models.CharField(max_length=100,default='')
	userprofile_email = models.CharField(max_length=100,default='')
	userprofile_dob = models.CharField(max_length=100,default='')
	userprofile_phoneno = models.CharField(max_length=100,default='')
	userprofile_password = models.CharField(max_length=500,default='')
	userprofile_conpassword = models.CharField(max_length=100,default='')

    