# Generated by Django 3.1.6 on 2021-02-22 23:48

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=stdimage.models.StdImageField(blank=True, help_text='Tamaño recomendado 350 X 350', null=True, upload_to='Usuarios'),
        ),
    ]
