# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-14 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantillas', '0003_auto_20171014_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantilla',
            name='fase',
            field=models.CharField(choices=[('Primer prueba de calidad de agua', 'Primer prueba de calidad de agua'), ('Inicio de trabajo', 'Inicio de trabajo'), ('Visita de acuerdos', 'Visita de acuerdos'), ('Construcción e instalación de Sistema bebedero', 'Construcción e instalación de Sistema bebedero'), ('Segunda prueba de calidad de agua', 'Segunda prueba de calidad de agua'), ('Inicio de funcionamiento', 'Inicio de funcionamiento'), ('Mantenimiento', 'Mantenimiento')], max_length=100),
        ),
    ]
