# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-26 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bebederos', '0010_sistemabebedero_modulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SistemaPotabilizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=10)),
                ('litros_de_vida', models.IntegerField()),
                ('presion', models.CharField(max_length=30, verbose_name='Presión')),
            ],
            options={
                'ordering': ['modelo'],
            },
        ),
        migrations.RemoveField(
            model_name='sistemabebedero',
            name='filtro',
        ),
        migrations.DeleteModel(
            name='Filtro',
        ),
        migrations.AddField(
            model_name='sistemabebedero',
            name='sistema_de_potabilizacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bebederos.SistemaPotabilizacion'),
        ),
    ]
