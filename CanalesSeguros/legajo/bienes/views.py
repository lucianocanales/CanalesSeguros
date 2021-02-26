# from django.shortcuts import render

from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import BienesPersonales, Motorizados, Bicicleta
from .models import Telefono, Vivienda, Accesorio
from .forms import BicicletaForm, AccesorioForm

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

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('login')

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.usuario_bien = self.request.user
        app_model.save()
        return super().form_valid(form)


class BicicletaUpdateView(UpdateView):
    model = Bicicleta
    template_name = "update/update_bici.html"
    form_class = BicicletaForm
    success_url = reverse_lazy('bienes')

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            if Bicicleta.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = Bicicleta.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.usuario_bien = self.request.user
        app_model.save()
        return super().form_valid(form)


class BicicletaDeleteView(DeleteView):
    model = Bicicleta
    template_name = "delete/delete_bici.html"
    success_url = reverse_lazy('bienes')

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            if Bicicleta.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = Bicicleta.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')


class AccesorioCreateView(CreateView):
    model = Accesorio
    template_name = "create/create_accesorio.html"
    form_class = AccesorioForm
    success_url = reverse_lazy('bienes')

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            if BienesPersonales.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = BienesPersonales.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def form_valid(self, form):
        form.instance.bien_id = self.kwargs['pk']
        return super().form_valid(form)
