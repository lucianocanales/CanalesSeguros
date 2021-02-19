from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from localflavor.ar.forms import ARDNIField
from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(UserCreationForm):

    email = forms.EmailField(
        max_length=254, help_text='Requerido para validar su email.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
