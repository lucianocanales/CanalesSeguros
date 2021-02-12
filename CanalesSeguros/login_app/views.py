from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


class Login(LoginView):
    template_name = 'login_app/login.html'
    redirect_authenticated_user = True
