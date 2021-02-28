from django.db import models
from localflavor.ar.ar_provinces import PROVINCE_CHOICES
import datetime

# Create your models here.

tipo_motorizado = [
    ('auto', 'Auto'),
    ('moto', 'Moto'),
    ('camion', 'Camion'),
]
tipo_vivienda = [
    ('depto en 3er piso o superior', 'Depto en 3er piso o superior'),
    ('casa', 'Casa o Depto en planta baja, 1er, 2do piso'),
    ('barrio privado', 'Barrio Privado'),
    ('casa de finde', 'Casa de fin de semana (no en barrio privado)'),
    ('negocio', 'Negocio'),
]
usos_choices = [
    ('privado', 'Privado'),
    ('comercial', 'Comercial'),
]


class BienesPersonales(models.Model):
    valor = models.IntegerField(verbose_name='Valor', default=0)
    usuario_bien = models.ForeignKey(
        "core.User",
        verbose_name='Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    uso = models.CharField(
        verbose_name='Uso',
        max_length=50,
        choices=usos_choices,
        default='privado'
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Vehiculo(BienesPersonales):

    marca = models.CharField(verbose_name="Marca", max_length=50)
    modelo = models.CharField(verbose_name="Modelo", max_length=50)
    chasis = models.CharField(verbose_name="Numero de chasis", max_length=25)

    def __str__(self):
        return self.marca + ' ' + self.modelo


class Accesorio(models.Model):

    nombre = models.CharField(verbose_name='Nombre', max_length=50)

    marca = models.CharField(
        verbose_name='Marca',
        max_length=50,
        null=True,
        blank=True,
    )

    modelo = models.CharField(
        verbose_name='Modelo',
        max_length=50,
        null=True,
        blank=True,
    )

    bien = models.ForeignKey(
        BienesPersonales,
        verbose_name='Bien Personal',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    serial_number = models.CharField(
        verbose_name='Numero de serie',
        max_length=100,
        help_text='Si es que tiene',
        null=True,
        unique=True,
        blank=True,
    )
    valor = models.IntegerField(verbose_name='Valor', default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.nombre + ' ' + self.serial_number

    class Meta:
        verbose_name = 'Accesorio'
        verbose_name_plural = 'Accesorios'


class Motorizados(Vehiculo):
    YEAR_CHOICES = []
    for r in range(1970, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))
    tipo = models.CharField(
        verbose_name='tipo',
        max_length=50,
        choices=tipo_motorizado,
        default='auto'
    )
    year = models.PositiveIntegerField(
        verbose_name='Año', choices=YEAR_CHOICES)
    dominio = models.CharField(verbose_name='patente', max_length=7)
    motor = models.CharField(verbose_name='Numero de motor', max_length=50)
    titular = models.CharField(verbose_name='titular', max_length=150)
    dni = models.CharField(verbose_name='DNI', max_length=10)

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"

    def __str__(self):
        return self.dominio + ' ' + self.modelo


class Bicicleta(Vehiculo):
    tipo = models.CharField(
        verbose_name='tipo',
        max_length=50,
        default='bicicleta',
        auto_created=True
    )

    class Meta:
        verbose_name = 'Bicicleta'
        verbose_name_plural = 'Bicicletas'


class Telefono(BienesPersonales):
    tipo = models.CharField(
        verbose_name='tipo',
        max_length=50,
        default='telefono',
        auto_created=True
    )
    marca = models.CharField(verbose_name="Marca", max_length=50)
    modelo = models.CharField(verbose_name="Modelo", max_length=50)
    IME = models.CharField(verbose_name="IME", max_length=50)
    caracteristicas = models.TextField(
        verbose_name='Caracteristicas', blank=True, null=True)

    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'

    def __str__(self):
        return self.marca + ' ' + self.modelo


class Vivienda(BienesPersonales):
    tipo = models.CharField(
        verbose_name='tipo de vivenda',
        max_length=50,
        default='casa',
        choices=tipo_vivienda
    )

    metros = models.IntegerField(verbose_name='Superficie')
    zip_code = models.IntegerField(verbose_name='Codigo Postal')
    ciudad = models.CharField(verbose_name='Ciudad', max_length=50)
    provicia = models.CharField(
        verbose_name='Provincia',
        max_length=50,
        choices=PROVINCE_CHOICES,
    )
    direccion = models.CharField(verbose_name='Direccion', max_length=100)

    class Meta:
        verbose_name = 'Casa'
        verbose_name_plural = 'Casas'

    def __str__(self):
        return self.direccion
