from django.contrib.auth.forms import UserChangeForm
from django.forms import TextInput, FileInput, CheckboxInput
from django import forms

from core.models import User
from localflavor.ar.forms import ARPostalCodeField, ARProvinceSelect


class UpdateProfile(UserChangeForm):
    i_agree = forms.BooleanField()
    provincia = ARProvinceSelect()
    zip_code = ARPostalCodeField()

    class Meta:
        model = User
        widgets = {


            'phone': TextInput(
                attrs={
                    'data-inputmask': '"mask": "9999 999999999"',
                    'placeholder': "9999 999999999",
                    'data-mask': "on",
                }
            ),
            'cuit': TextInput(
                attrs={
                    'data-inputmask': '"mask": "99-99999999-9"',
                    'data-mask': "on",
                }
            ),
            'dni': TextInput(
                attrs={
                    'data-inputmask': '"mask": "99.999.999"',
                    'data-mask': "on",
                }
            ),
            'avatar':  FileInput(
                attrs={
                    'class': 'custom-file-input form-control',
                    'id': "exampleInputFile",
                }
            )
        }

        fields = (
            'avatar',
            'username',
            'email',
            'first_name',
            'last_name',
            'birth_date',
            'dni',
            'cuit',
            'ciudad',
            'provincia',
            'zip_code',
            'bio',
            'phone',
        )
