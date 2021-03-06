from django import template
from localflavor.ar.ar_provinces import PROVINCE_CHOICES

register = template.Library()


def provincia_completo(letra):
    for provinca in PROVINCE_CHOICES:
        if letra.lower() == provinca[0].lower():
            return provinca[1]
        else:
            return letra


register.filter('provincia_completo', provincia_completo)
