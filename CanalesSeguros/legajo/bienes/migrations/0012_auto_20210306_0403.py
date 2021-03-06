# Generated by Django 3.1.6 on 2021-03-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienes', '0011_auto_20210228_0448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vivienda',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='vivienda',
            name='provicia',
        ),
        migrations.RemoveField(
            model_name='vivienda',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='bienespersonales',
            name='ciudad',
            field=models.CharField(default='La Plata', max_length=50, verbose_name='Ciudad'),
        ),
        migrations.AddField(
            model_name='bienespersonales',
            name='provicia',
            field=models.CharField(choices=[('B', 'Buenos Aires'), ('K', 'Catamarca'), ('H', 'Chaco'), ('U', 'Chubut'), ('C', 'Ciudad Autónoma de Buenos Aires'), ('X', 'Córdoba'), ('W', 'Corrientes'), ('E', 'Entre Ríos'), ('P', 'Formosa'), ('Y', 'Jujuy'), ('L', 'La Pampa'), ('F', 'La Rioja'), ('M', 'Mendoza'), ('N', 'Misiones'), ('Q', 'Neuquén'), ('R', 'Río Negro'), ('A', 'Salta'), ('J', 'San Juan'), ('D', 'San Luis'), ('Z', 'Santa Cruz'), ('S', 'Santa Fe'), ('G', 'Santiago del Estero'), ('V', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'), ('T', 'Tucumán')], default='b', max_length=50, verbose_name='Provincia'),
        ),
        migrations.AddField(
            model_name='bienespersonales',
            name='zip_code',
            field=models.IntegerField(default=1900, verbose_name='Codigo Postal'),
        ),
    ]
