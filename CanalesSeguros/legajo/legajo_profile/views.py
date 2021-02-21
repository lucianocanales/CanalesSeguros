from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from core.models import User
from .forms import UpdateProfile
# Create your views here.


class UpdateProfileView(UpdateView):
    model = User
    form_class = UpdateProfile
    template_name = 'UpdateProfile.html'
    success_url = reverse_lazy('core:home')
