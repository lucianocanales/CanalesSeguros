from django import forms
from .models import Bicicleta, Accesorio, Motorizados


class AccesorioForm(forms.ModelForm):

    class Meta:
        model = Accesorio
        fields = '__all__'
        exclude = ('bien', )


class BicicletaForm(forms.ModelForm):

    class Meta:
        model = Bicicleta
        fields = '__all__'
        exclude = ('usuario_bien', )


class MotorizadosForm(forms.ModelForm):
    class Meta:
        model = Motorizados
        fields = '__all__'
        exclude = ('usuario_bien', 'tipo')
