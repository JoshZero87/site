# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-09 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local_groups', '0031_auto_20170309_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='issues',
            field=models.ManyToManyField(to='endorsements.Issue'),
        ),
    ]
