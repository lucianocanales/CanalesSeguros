# Generated by Django 3.1.6 on 2021-02-22 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210221_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Numero de telefono'),
        ),
    ]
