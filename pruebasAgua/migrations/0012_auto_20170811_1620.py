# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-11 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasAgua', '0011_auto_20170811_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='segundaprueba',
            name='acta_segunda_prueba',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/2/acta_de_segunda_prueba/%Y/%m/%d/', verbose_name='Acta de segunda prueba'),
        ),
        migrations.AddField(
            model_name='segundaprueba',
            name='dictamen_sistema_potabilizador',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/2/resultados/%Y/%m/%d/', verbose_name='Dictamen del sistema potabilizador a utilizar'),
        ),
        migrations.AddField(
            model_name='segundaprueba',
            name='dictamen_validacion',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/2/validacion/%Y/%m/%d/', verbose_name='Dictamen de validación'),
        ),
        migrations.AddField(
            model_name='segundaprueba',
            name='reporte_toma_agua',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/2/reporte_de_toma/%Y/%m/%d/', verbose_name='Reporte de toma de muestra'),
        ),
        migrations.AlterField(
            model_name='primerprueba',
            name='dictamen_validacion',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/1/validacion/%Y/%m/%d/', verbose_name='Dictamen de validación'),
        ),
        migrations.AlterField(
            model_name='primerprueba',
            name='reporte_toma_agua',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/1/reporte_de_toma/%Y/%m/%d/', verbose_name='Reporte de toma de muestra'),
        ),
        migrations.AlterField(
            model_name='segundaprueba',
            name='constancia_recepcion',
            field=models.FileField(upload_to='pruebas/2/constancia/%Y/%m/%d/', verbose_name='Constancia de recepción de muestra de laboratorio'),
        ),
        migrations.AlterField(
            model_name='segundaprueba',
            name='resultados',
            field=models.FileField(upload_to='pruebas/2/resultados/%Y/%m/%d/', verbose_name='Resultados de muestreo'),
        ),
        migrations.AlterField(
            model_name='segundaprueba',
            name='video',
            field=models.FileField(upload_to='pruebas/2/video/%Y/%m/%d/', verbose_name='Video'),
        ),
    ]
