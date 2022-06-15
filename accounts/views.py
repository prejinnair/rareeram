from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

# Create your views here.

# for admin login
from Rareeram import settings


class login(View):

    @staticmethod
    def post(request):
        login_email = request.POST['email']
        login_password = request.POST['password']

        if User.objects.filter(email=login_email).exists():
            user = User.objects.get(email=login_email)

            if user.check_password(login_password):

                if user and user.is_staff:
                    auth.login(request, user)
                    return redirect(settings.LOGIN_REDIRECT_URL)
                else:
                    messages.error(request, '! unauthorized user')
                    return render(request, 'accounts/login.html')

            else:
                messages.error(request, '! invalid password')
                return render(request, 'accounts/login.html')
        else:
            messages.error(request, '! invalid email')
            return render(request, 'accounts/login.html')

    @staticmethod
    def get(request):
        return render(request, 'accounts/login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')
