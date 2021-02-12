# Generated by Django 3.1.6 on 2021-02-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ciudad',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='user',
            name='provincia',
            field=models.CharField(default='B', max_length=1, verbose_name='Provicia'),
        ),
        migrations.AlterField(
            model_name='user',
            name='zip_code',
            field=models.IntegerField(default=0, verbose_name='Codigo Postal'),
        ),
    ]
