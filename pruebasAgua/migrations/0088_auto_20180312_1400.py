# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-12 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasAgua', '0087_auto_20180122_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='primerprueba',
            name='empresa_envio',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Empresa de envío de muestreo'),
        ),
        migrations.AddField(
            model_name='primerprueba',
            name='modalidad_envio',
            field=models.CharField(blank=True, choices=[('Validado', 'Validado'), ('No validado', 'No validado'), ('En espera', 'En espera')], max_length=11, null=True, verbose_name='Modalidad de envío'),
        ),
        migrations.AddField(
            model_name='primerprueba',
            name='no_rastreabilidad',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='No. de rastreabilidad'),
        ),
        migrations.AddField(
            model_name='primerprueba',
            name='rastreabilidad_interna_envio',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/1/rastreabilidad/%Y/%m/%d/', verbose_name='Rastreabilidad de envío de muestreo'),
        ),
        migrations.AddField(
            model_name='primerprueba',
            name='rastreabilidad_interna_recepcion',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/1/rastreabilidad/%Y/%m/%d/', verbose_name='Rastreabilidad de recepcíon de muestreo'),
        ),
        migrations.AlterField(
            model_name='primerprueba',
            name='foto_toma_agua_2',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/1/fotos/%Y/%m/%d/', verbose_name='Fotografía de muestra en el punto de muestreo'),
        ),
    ]
