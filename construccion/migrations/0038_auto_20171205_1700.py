# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-05 23:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('construccion', '0037_auto_20171205_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvolventeTerminado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='evidencia/envolvente/%Y/%m/%d/', verbose_name='Video')),
                ('escuela', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='escuela_instalacion_bebedero', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Instalaciones de Sistemas Bebedero',
                'ordering': ['escuela'],
            },
        ),
        migrations.RemoveField(
            model_name='instalacionbebedero',
            name='escuela',
        ),
        migrations.RemoveField(
            model_name='evidenciaconstruccion',
            name='video',
        ),
        migrations.AddField(
            model_name='evidenciaconstruccion',
            name='foto',
            field=models.FileField(default='default.pdf', upload_to='evidencia/foto/%Y/%m/%d/', verbose_name='Fotografía'),
        ),
        migrations.DeleteModel(
            name='InstalacionBebedero',
        ),
    ]
