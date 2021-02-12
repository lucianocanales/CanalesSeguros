from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage import StdImageField


class User(AbstractUser):
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
        default='B'
    )
    zip_code = models.IntegerField(verbose_name='Codigo Postal', default=0)
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Fecha de nacimiento'
    )
    avatar = StdImageField(
        variations={
            'medium': (350, 350),
            'thumbnail': (100, 100),
        },
        delete_orphans=True,
        help_text='Tamaño recomendado 350 X 350',
        upload_to='productos',
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
