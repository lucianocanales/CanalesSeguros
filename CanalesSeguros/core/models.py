from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage import StdImageField
from localflavor.ar.ar_provinces import PROVINCE_CHOICES


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Descripcion',
        null=True
    )
    ciudad = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Direccion'
    )
    provincia = models.CharField(
        max_length=1,
        verbose_name='Provicia',
        choices=PROVINCE_CHOICES,
        default='B'
    )
    zip_code = models.IntegerField(
        verbose_name='Codigo Postal',
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name='Numero de telefono',
        max_length=14,
        blank=True,
        null=True
    )
    birth_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Fecha de nacimiento'
    )
    avatar = StdImageField(
        variations={
            'medium': (350, 350),
            'thumbnail': (100, 100, True),
        },
        delete_orphans=True,
        help_text='Tamaño recomendado 350 X 350',
        upload_to='Usuarios',
        null=True,
        blank=True
    )
    dni = models.CharField(
        max_length=10,
        verbose_name='DNI',
        unique=True,
        blank=True,
        null=True
    )
    cuit = models.CharField(
        max_length=13,
        verbose_name='CUIT',
        blank=True,
        null=True
    )
