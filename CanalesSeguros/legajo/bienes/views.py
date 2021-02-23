# from django.shortcuts import render
from django.views.generic import ListView
from .models import Vehiculo

# Create your views here.


class BienesListView(ListView):
    model = Vehiculo
    template_name = "bienes.html"
