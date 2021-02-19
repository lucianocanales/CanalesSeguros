from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

# Create your views here.


class Login(LoginView):
    template_name = 'login_app/login.html'
    redirect_authenticated_user = True


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
