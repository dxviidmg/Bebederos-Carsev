# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-27 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasAgua', '0013_remove_segundaprueba_dictamen_sistema_potabilizador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primerprueba',
            name='constancia_recepcion',
        ),
        migrations.RemoveField(
            model_name='primerprueba',
            name='dictamen_validacion',
        ),
        migrations.RemoveField(
            model_name='primerprueba',
            name='resultados',
        ),
        migrations.AddField(
            model_name='primerprueba',
            name='resultados_inifed',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name='Resultados de analísis para INIFED'),
        ),
        migrations.AddField(
            model_name='primerprueba',
            name='resultados_laboratorio',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name='Resultados de analísis de laboratorio'),
        ),
        migrations.AddField(
            model_name='primerprueba',
            name='sugerencias_sp',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name='Sugerencia de sistema potabilizador'),
        ),
        migrations.AlterField(
            model_name='primerprueba',
            name='video',
            field=models.FileField(upload_to='pruebas/1/video/%Y/%m/%d/', verbose_name='Video de toma de agua'),
        ),
    ]
