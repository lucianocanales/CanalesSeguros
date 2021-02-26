from django import forms
from .models import Bicicleta, Accesorio


class AccesorioInline(forms.ModelForm):

    class Meta:
        model = Accesorio
        fields = '__all__'


class BicicletaForm(forms.ModelForm):
    accesorios = AccesorioInline()
    prefix = 'accesorios'

    class Meta:
        model = Bicicleta
        fields = '__all__'


BicicletaInlineFormset = forms.inlineformset_factory(
    Bicicleta,
    Accesorio,
    fields=('nombre', 'marca', 'modelo', 'serial_number'),

    extra=2,
    can_delete=False
)
