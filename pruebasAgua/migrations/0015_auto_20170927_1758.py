# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-27 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasAgua', '0014_auto_20170927_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primerprueba',
            name='sugerencias_sp',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name='Sugerencia de Sistema Potabilizador'),
        ),
    ]
