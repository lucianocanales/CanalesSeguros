from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetView
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


# Create your views here.


class Login(LoginView):
    template_name = 'login_app/login.html'
    redirect_authenticated_user = True


class ForgotPassword(PasswordResetView):
    template_name = 'registration/clave_reset_form.html'
    email_template_name = 'registration/clave_reset_email.html'
    subject_template_name = 'registration/clave_reset_subject.txt'
    success_url = 'done/'


class RecoverPassword (PasswordResetConfirmView):
    template_name = 'registration/clave_reset_confirm.html'
    success_url = reverse_lazy('password_reset')

    # post_reset_login = True


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'login_app/register.html', {'form': form})
