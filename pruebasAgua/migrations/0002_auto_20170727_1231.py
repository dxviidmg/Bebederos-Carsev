# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 17:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pruebasAgua', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SegundaPrueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constancia_de_recepcion', models.FileField(upload_to='pruebas/1/constancia/%Y/%m/%d/', verbose_name='Constancia de recepción de muestra de laboratorio')),
                ('video', models.FileField(upload_to='pruebas/1/video/%Y/%m/%d/', verbose_name='Video')),
                ('resultados', models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name='Resultados')),
                ('creacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación')),
                ('escuela', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_segunda_prueba', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='primerprueba',
            name='laboratorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_primer_prueba', to=settings.AUTH_USER_MODEL),
        ),
    ]
