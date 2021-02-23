from django.db import models

# Create your models here.
tipo_bien = {
    'auto': 'Auto',
    'moto': 'Moto',
    'camion': 'Camion',
    'bicicleta': 'Bicicleta',
    'telefono': 'Telefono',
    'casa': 'Casa',
    'negocio': 'Negocio',
}
usos_choices = {
    'privado': 'Privado',
    'comercial': 'Comercial',

}


class BienesPersonales(models.Model):

    usuario_bien = models.ForeignKey(
        "core.User",
        verbose_name='Usuario',
        on_delete=models.CASCADE
    )

    uso = models.CharField(
        verbose_name='Uso',
        max_length=50,
        choices=usos_choices,
        default='privado'
    )

    is_active = models.BooleanField(verbose_name="Borrar", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Vehiculo(BienesPersonales):

    marca = models.CharField(verbose_name="Marca", max_length=50)
    modelo = models.CharField(verbose_name="Modelo", max_length=50)
    chasis = models.CharField(verbose_name="Numero de chasis", max_length=25)

    tipo = models.CharField(verbose_name='Tipo', max_length=50)

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"

    def __str__(self):
        return self.marca + ' ' + self.modelo


class Motorizados(Vehiculo):
    dominio = models.CharField(verbose_name='patente', max_length=7)
    motor = models.CharField(verbose_name='Numero de motor', max_length=50)
    titular = models.CharField(verbose_name='titular', max_length=150)
    dni = models.CharField(verbose_name='DNI', max_length=10)

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

    def __str__(self):
        return self.dominio + ' ' + self.modelo


class Bicicleta(Vehiculo):

    class Meta:
        verbose_name = 'Bicicleta'
        verbose_name_plural = 'Bicicletas'


class Telefono(BienesPersonales):
    marca = models.CharField(verbose_name="Marca", max_length=50)
    modelo = models.CharField(verbose_name="Modelo", max_length=50)
    IME = models.CharField(verbose_name="Marca", max_length=50)
    caracteristicas = models.TextField(verbose_name='Caracteristicas')

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

    def __str__(self):
        return self.marca + ' ' + self.modelo
