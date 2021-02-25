# from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
# from core.models import User
from .models import BienesPersonales, Motorizados, Bicicleta
from .models import Telefono, Vivienda
from .forms import BicicletaForm, BicicletaInlineFormset
from django.urls import reverse_lazy

# Create your views here.


class BienesListView(ListView):
    model = BienesPersonales
    template_name = "bienes.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bienes Personales'
        context["vehiculo"] = Motorizados.objects.filter(
            usuario_bien=self.request.user)
        context['bicicleta'] = Bicicleta.objects.filter(
            usuario_bien=self.request.user)
        context['telefono'] = Telefono.objects.filter(
            usuario_bien=self.request.user)
        context['vivienda'] = Vivienda.objects.filter(
            usuario_bien=self.request.user)
        return context


class BicicletaCreateView(CreateView):
    model = Bicicleta
    template_name = "create/create_bicicleta.html"
    form_class = BicicletaForm
    success_url = reverse_lazy('bienes')
