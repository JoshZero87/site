# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-07 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local_groups', '0021_auto_20170306_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='latitude',
            field=models.FloatField(default=38.897539, verbose_name='Latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='longitude',
            field=models.FloatField(default=-77.003308, verbose_name='Longitude'),
            preserve_default=False,
        ),
    ]
