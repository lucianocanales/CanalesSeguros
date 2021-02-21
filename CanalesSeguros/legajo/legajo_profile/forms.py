from django.contrib.auth.forms import UserChangeForm

from core.models import User
from localflavor.ar.forms import ARCUITField, ARDNIField
from localflavor.ar.forms import ARPostalCodeField, ARProvinceSelect


class UpdateProfile(UserChangeForm):
    provincia = ARProvinceSelect()
    zip_code = ARPostalCodeField()
    dni = ARDNIField()
    cuit = ARCUITField()

    class Meta:
        model = User
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
        )
