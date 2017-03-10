# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-09 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('local_groups', '0034_auto_20170309_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='state_province',
            new_name='meeting_state_province',
        ),
        migrations.RemoveField(
            model_name='group',
            name='recurring_meeting_location',
        ),
        migrations.AlterField(
            model_name='group',
            name='meeting_address_line1',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Address Line 1'),
        ),
        migrations.AlterField(
            model_name='group',
            name='meeting_address_line2',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AlterField(
            model_name='group',
            name='meeting_city',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='group',
            name='meeting_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Country'),
        ),
    ]
