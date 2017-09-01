# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-01 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_region_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='tipo',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('SI', 'Superintendente'), ('Ejecutora', 'Ejecutora'), ('Escuela', 'Escuela'), ('Laboratorio', 'Laboratorio'), ('INIFED', 'INIFED'), ('IMTA', 'IMTA'), ('ECA', 'Residente Técnico de Calidad de Agua')], max_length=30),
        ),
    ]
