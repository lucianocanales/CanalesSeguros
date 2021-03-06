
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.urls.base import reverse
from django.views.generic import ListView, CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView, DetailView


from .models import BienesPersonales, Motorizados, Bicicleta
from .models import Telefono, Vivienda, Accesorio
from .forms import BicicletaForm, AccesorioForm, MotorizadosForm
from .forms import TelefonoForm, ViviendaForm


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

#############################################
# vistas de bicicletas
#############################################


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Bicicleta'
        return context


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

    def get_success_url(self):
        next = self.request.POST.get('next', reverse('bienes'))
        return next

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.usuario_bien = self.request.user
        app_model.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Bicicleta'
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Bicicleta'
        return context


class BicicletaDetailView(DetailView):
    model = Bicicleta
    context_object_name = 'bicicleta'
    template_name = "detail/detail_bici.html"

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Detalle del bien Personal'
        context["accesorios"] = Accesorio.objects.filter(
            bien_id=self.kwargs['pk'])
        return context


#############################################
# vistas de vehiculos
#############################################


class MotorizadosCreateView(CreateView):
    model = Motorizados
    template_name = 'create/create_motorizado.html'
    form_class = MotorizadosForm
    success_url = reverse_lazy('bienes')

    def dispatch(self, request, *args, **kwargs):

        tipos_motor = ['moto', 'auto', 'camion']
        if self.request.user.is_authenticated:
            if self.kwargs['tipo'] in tipos_motor:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def form_valid(self, form):

        app_model = form.save(commit=False)
        app_model.usuario_bien = self.request.user
        app_model.tipo = self.kwargs['tipo']

        app_model.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear ' + self.kwargs['tipo'].capitalize()
        return context


class MotorizadosUpdateView(UpdateView):
    model = Motorizados
    template_name = "update/update_motodizado.html"
    form_class = MotorizadosForm
    success_url = reverse_lazy('bienes')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if Motorizados.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = Motorizados.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def get_success_url(self):
        next = self.request.POST.get('next', reverse('bienes'))
        return next

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipe = Motorizados.objects.get(
            id=self.kwargs['pk']).tipo
        context['title'] = 'Actualizar ' + tipe.capitalize()
        return context


class MotorizadosDeleteView(DeleteView):
    model = Motorizados
    template_name = "delete/delete_motorizado.html"
    success_url = reverse_lazy('bienes')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if Motorizados.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = Motorizados.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipe = Motorizados.objects.get(
            id=self.kwargs['pk']).tipo
        context['title'] = 'Eliminar ' + tipe.capitalize()
        return context


class MotorizadosDetailView(DetailView):
    model = Motorizados
    context_object_name = 'motorizados'
    template_name = "detail/detail_motorizados.html"

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            if Motorizados.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = Motorizados.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        marca = Motorizados.objects.get(id=self.kwargs['pk']).marca
        modelo = Motorizados.objects.get(id=self.kwargs['pk']).modelo
        dominio = Motorizados.objects.get(id=self.kwargs['pk']).dominio
        context['title'] = marca + ' - ' + modelo + ' - ' + dominio
        context["accesorios"] = Accesorio.objects.filter(
            bien_id=self.kwargs['pk'])
        tipo = Motorizados.objects.get(id=self.kwargs['pk']).tipo
        if tipo == 'auto':
            context["tipoIcon"] = 'fa-car'
        elif tipo == 'moto':
            context["tipoIcon"] = 'fa-motorcycle'
        elif tipo == 'camion':
            context["tipoIcon"] = 'fa-truck-moving'
        return context

#############################################
# vistas de telefono
#############################################


class TelefonoCreateView(CreateView):
    model = Telefono
    template_name = "create/create_telefono.html"
    form_class = TelefonoForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Telefono'
        return context


class TelefonoUpdateView(UpdateView):
    model = Telefono
    template_name = "update/update_telefono.html"
    form_class = TelefonoForm
    success_url = reverse_lazy('bienes')

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            if Telefono.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = Telefono.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def get_success_url(self):
        next = self.request.POST.get('next', reverse('bienes'))
        return next

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.usuario_bien = self.request.user
        app_model.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Telefono'
        return context


class TelefonoDeleteView(DeleteView):
    model = Telefono
    template_name = "create/create_telefono.html"
    success_url = reverse_lazy('bienes')

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            if Telefono.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = Telefono.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Telefono'
        return context


class TelefonoDetailView(DetailView):
    model = Telefono
    context_object_name = 'telefono'
    template_name = "detail/detail_telefono.html"

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            if Telefono.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = Telefono.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        marca = Telefono.objects.get(id=self.kwargs['pk']).marca
        modelo = Telefono.objects.get(id=self.kwargs['pk']).modelo
        context['title'] = marca + ' - ' + modelo
        return context

#############################################
# vistas de viviendas
#############################################


class ViviendaCreateView(CreateView):
    model = Vivienda
    template_name = 'create/create_vivienda.html'
    form_class = ViviendaForm
    success_url = reverse_lazy('bienes')

    def dispatch(self, request, *args, **kwargs):

        tipos_motor = ['casa', 'negocio']
        if self.request.user.is_authenticated:
            if self.kwargs['tipo'] in tipos_motor:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def form_valid(self, form):

        app_model = form.save(commit=False)
        app_model.usuario_bien = self.request.user

        if self.kwargs['tipo'] == 'negocio':
            app_model.uso = 'comercial'
            app_model.tipo = 'negocio'
        else:
            app_model.uso = 'privado'
        app_model.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear ' + self.kwargs['tipo'].capitalize()
        return context


class ViviendaUpdateView(UpdateView):
    model = Vivienda
    template_name = "update/update_vivienda.html"
    form_class = ViviendaForm
    success_url = reverse_lazy('bienes')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if Vivienda.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = Vivienda.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def get_success_url(self):
        next = self.request.POST.get('next', reverse('bienes'))
        return next

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipe = Vivienda.objects.get(
            id=self.kwargs['pk']).tipo
        context['title'] = 'Actualizar ' + tipe.capitalize()
        return context


class ViviendaDeleteView(DeleteView):
    model = Vivienda
    template_name = "delete/delete_vivienda.html"
    success_url = reverse_lazy('bienes')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if Vivienda.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = Vivienda.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipe = Vivienda.objects.get(
            id=self.kwargs['pk']).tipo
        context['title'] = 'Eliminar ' + tipe.capitalize()
        return context


class ViviendaDetailView(DetailView):
    model = Vivienda
    context_object_name = 'vivienda'
    template_name = "detail/detail_vivienda.html"

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            if Vivienda.objects.filter(
                    id=self.kwargs['pk']).exists():
                owner = Vivienda.objects.get(
                    id=self.kwargs['pk']).usuario_bien
                if owner == self.request.user:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('bienes')
            else:
                return redirect('bienes')
        else:
            return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        direccion = Vivienda.objects.get(id=self.kwargs['pk']).direccion
        context['title'] = direccion
        context["accesorios"] = Accesorio.objects.filter(
            bien_id=self.kwargs['pk'])
        tipo = Vivienda.objects.get(id=self.kwargs['pk']).tipo
        if tipo == 'depto en 3er piso o superior':
            context['tipoIcon'] = 'fa-building'
        elif tipo == 'casa' or tipo == 'barrio privado':
            context['tipoIcon'] = 'fa-home'
        elif tipo == 'casa de finde':
            context['tipoIcon'] = 'fa-umbrella-beach'
        elif tipo == 'negocio':
            context['tipoIcon'] = 'fa-store-alt'

        return context

#############################################
# vistas de Accesorios
#############################################


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

    def get_success_url(self):
        next = self.request.POST.get('next', reverse('bienes'))
        return next

    def form_valid(self, form):
        form.instance.bien_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Accesori'
        return context
