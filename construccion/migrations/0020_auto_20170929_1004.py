# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-29 15:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('construccion', '0019_auto_20170911_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacionbebedero',
            name='memoria_calculo',
            field=models.FileField(default='default.pdf', upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name='Memorias de calculo'),
        ),
        migrations.AlterField(
            model_name='instalacionbebedero',
            name='plano_instalacion',
            field=models.FileField(default='default.pdf', upload_to='instalaciones/planos/%Y/%m/%d/', verbose_name='Plano de Instalaciones'),
        ),
        migrations.AlterField(
            model_name='instalacionbebedero',
            name='si',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sim_instalacion_sb', to=settings.AUTH_USER_MODEL, verbose_name='Superintendente'),
        ),
        migrations.AlterField(
            model_name='instalacionbebedero',
            name='trabajos_de_conexion',
            field=models.FileField(default='default.pdf', upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name='Trabajos de conexión'),
        ),
    ]
