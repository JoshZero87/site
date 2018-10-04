# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-02 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominations', '0082_auto_20180626_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='nominationsplatformalert',
            name='alert_level',
            field=models.IntegerField(blank=True, choices=[(1, 'success'), (2, 'info'), (3, 'warning'), (4, 'danger')], default=2),
        ),
    ]
