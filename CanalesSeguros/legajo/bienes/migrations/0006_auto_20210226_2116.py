# Generated by Django 3.1.6 on 2021-02-27 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bienes', '0005_auto_20210226_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesorio',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='bienespersonales',
            name='is_active',
        ),
    ]