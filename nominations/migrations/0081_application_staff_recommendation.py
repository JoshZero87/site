# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-05-10 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominations', '0080_initiativeapplication_auth_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='staff_recommendation',
            field=models.IntegerField(blank=True, choices=[(1, 'Recommend to Endorse'), (2, 'Recommend Not to Endorse'), (3, 'No Recommendation')], null=True),
        ),
    ]
