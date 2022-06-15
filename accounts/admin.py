from django.contrib import admin
from accounts.models import UserAuthentication
# Register your models here.
from django.contrib.auth.admin import UserAdmin
# from .models import User
#
#
# class UserDetailsAdmin(UserAdmin):
#     list_display = (
#         'username', 'email', 'first_name', 'last_name', 'device_token','is_active'
#     )
#
#
# admin.site.register(User, UserDetailsAdmin)


admin.site.register(UserAuthentication)