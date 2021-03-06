from django import forms
from .models import Bicicleta, Accesorio, Motorizados, Telefono, Vivienda


class AccesorioForm(forms.ModelForm):

    class Meta:
        model = Accesorio
        fields = '__all__'
        exclude = ('bien', 'valor')


class BicicletaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Bicicleta
        fields = '__all__'
        exclude = ('usuario_bien', 'valor', 'tipo')


class MotorizadosForm(forms.ModelForm):
    class Meta:
        model = Motorizados
        fields = '__all__'
        exclude = ('usuario_bien', 'tipo', 'valor')


class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = '__all__'
        exclude = ('usuario_bien', 'tipo', 'valor')


class ViviendaForm(forms.ModelForm):
    class Meta:
        model = Vivienda
        fields = '__all__'
        exclude = ('usuario_bien', 'uso')
