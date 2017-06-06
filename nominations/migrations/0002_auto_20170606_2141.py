# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-06 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('nominations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='candidate_first_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Candidate First Name'),
        ),
        migrations.AddField(
            model_name='application',
            name='candidate_last_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Candidate Last Name'),
        ),
        migrations.AddField(
            model_name='application',
            name='candidate_office',
            field=models.CharField(max_length=255, null=True, verbose_name='Candidate Office'),
        ),
        migrations.AddField(
            model_name='application',
            name='candidate_state',
            field=localflavor.us.models.USStateField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='group_id',
            field=models.CharField(max_length=4, null=True, verbose_name='Group ID'),
        ),
        migrations.AddField(
            model_name='application',
            name='group_name',
            field=models.CharField(max_length=64, null=True, verbose_name='Group Name'),
        ),
        migrations.AddField(
            model_name='application',
            name='rep_email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Contact Email'),
        ),
        migrations.AddField(
            model_name='application',
            name='rep_first_name',
            field=models.CharField(max_length=35, null=True, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='application',
            name='rep_last_name',
            field=models.CharField(max_length=35, null=True, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='application',
            name='rep_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, verbose_name='Phone Number'),
        ),
    ]
