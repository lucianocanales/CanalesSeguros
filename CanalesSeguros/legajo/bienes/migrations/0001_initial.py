# Generated by Django 3.1.6 on 2021-02-24 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BienesPersonales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso', models.CharField(choices=[('privado', 'Privado'), ('comercial', 'Comercial')], default='privado', max_length=50, verbose_name='Uso')),
                ('is_active', models.BooleanField(default=False, verbose_name='Borrar')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('usuario_bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('bienespersonales_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bienes.bienespersonales')),
                ('metros', models.IntegerField(verbose_name='Metros Cubiertos')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
            ],
            bases=('bienes.bienespersonales',),
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('bienespersonales_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bienes.bienespersonales')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('IME', models.CharField(max_length=50, verbose_name='Marca')),
                ('caracteristicas', models.TextField(verbose_name='Caracteristicas')),
            ],
            options={
                'verbose_name': 'Auto',
                'verbose_name_plural': 'Autos',
            },
            bases=('bienes.bienespersonales',),
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('bienespersonales_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bienes.bienespersonales')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('chasis', models.CharField(max_length=25, verbose_name='Numero de chasis')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
            },
            bases=('bienes.bienespersonales',),
        ),
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('marca', models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca')),
                ('modelo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Modelo')),
                ('serial_number', models.CharField(blank=True, help_text='Si es que tiene', max_length=100, null=True, unique=True, verbose_name='Numero de serie')),
                ('is_active', models.BooleanField(default=False, verbose_name='Borrar')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bienes.bienespersonales', verbose_name='Bien Personal')),
            ],
            options={
                'verbose_name': 'Accesorio',
                'verbose_name_plural': 'Accesorios',
            },
        ),
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bienes.vehiculo')),
            ],
            options={
                'verbose_name': 'Bicicleta',
                'verbose_name_plural': 'Bicicletas',
            },
            bases=('bienes.vehiculo',),
        ),
        migrations.CreateModel(
            name='Motorizados',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bienes.vehiculo')),
                ('dominio', models.CharField(max_length=7, verbose_name='patente')),
                ('motor', models.CharField(max_length=50, verbose_name='Numero de motor')),
                ('titular', models.CharField(max_length=150, verbose_name='titular')),
                ('dni', models.CharField(max_length=10, verbose_name='DNI')),
            ],
            options={
                'verbose_name': 'Auto',
                'verbose_name_plural': 'Autos',
            },
            bases=('bienes.vehiculo',),
        ),
    ]
