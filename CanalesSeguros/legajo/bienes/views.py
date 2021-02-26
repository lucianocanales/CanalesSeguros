# from django.shortcuts import render

from django.shortcuts import redirect, render, HttpResponseRedirect, render_to_response
from django.views.generic import ListView
from core.models import User
from .models import BienesPersonales, Motorizados, Bicicleta
from .models import Telefono, Vivienda, Accesorio
from .forms import AccesorioInline, BicicletaForm
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
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


def BicicletaCreateView(request, id):
    if id:
        bici = Bicicleta.objects.get(pk=bici_id)
    else:
        bici = Bicicleta()

    bici_form = BicicletaForm(instance=bici)
    AccesorioInlineFormSet = inlineformset_factory(
        Bicicleta,
        Accesorio,
        fields=('nombre', 'marca', 'modelo', 'serial_number'),
        extra=2,
        can_delete=False
    )
    formset = AccesorioInlineFormSet(isinstance=bici)

    if request.method == "POST":
        bici_form = BicicletaForm(request.POST)
        if id:
            bici_form = BicicletaForm(request.POST, instance=bici)

        if bici_form.is_valid():
            created_bici = bici_form.save(commit=False)
            formset = AccesorioInlineFormSet(
                request.POST, request.FILES, isinstance=created_bici)
            if formset.is_valid():
                created_bici.save()
                formset.save()
                return HttpResponseRedirect(created_bici.get_absolute_url())
    return render_to_response("create/create_bicicleta.html", {
        "bici_form": bici_form,
        "formset": formset,
    })
    # return render(request, 'create/create_bicicleta.html')
