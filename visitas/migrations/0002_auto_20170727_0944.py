# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 14:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visitas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SegundaVisita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acta_acuerdos', models.FileField(upload_to='visitas/2/acta/%Y/%m/%d/', verbose_name='Acta de acuerdos y ubicación del módulo')),
                ('reporte_de_toma', models.FileField(upload_to='visitas/2/reporte_de_toma/%Y/%m/%d/', verbose_name='Reporte de toma de muestra')),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['escuela'],
            },
        ),
        migrations.AlterField(
            model_name='primervisita',
            name='agenda',
            field=models.FileField(upload_to='visitas/1/agenda/%Y/%m/%d/', verbose_name='Agenda'),
        ),
        migrations.AlterField(
            model_name='primervisita',
            name='constancia_de_visita',
            field=models.FileField(upload_to='visitas/1/constancia/%Y/%m/%d/', verbose_name='Constancia de visita'),
        ),
        migrations.AlterField(
            model_name='primervisita',
            name='hoja_de_cotizacion',
            field=models.FileField(upload_to='visitas/1/cotizacion/%Y/%m/%d/', verbose_name='Hoja de cotizaciones'),
        ),
        migrations.AlterField(
            model_name='primervisita',
            name='membrete_para_mail',
            field=models.FileField(upload_to='visitas/1/membrete/%Y/%m/%d/', verbose_name='Membrete para e-mail'),
        ),
        migrations.AlterField(
            model_name='primervisita',
            name='plantilla_fotografica',
            field=models.FileField(upload_to='visitas/1/plantilla/%Y/%m/%d/', verbose_name='Plantilla fotografica'),
        ),
    ]
