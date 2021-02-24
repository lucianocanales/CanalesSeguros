# from django.shortcuts import render
from django.views.generic import ListView
from core.models import User

# Create your views here.


class BienesListView(ListView):
    model = User
    template_name = "bienes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehiculo"] =
        return context
