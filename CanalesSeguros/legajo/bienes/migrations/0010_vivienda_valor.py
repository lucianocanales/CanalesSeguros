# Generated by Django 3.1.6 on 2021-02-28 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienes', '0009_auto_20210228_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='vivienda',
            name='valor',
            field=models.IntegerField(default=0, verbose_name='Valor'),
        ),
    ]