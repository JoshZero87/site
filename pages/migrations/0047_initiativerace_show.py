# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-07 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0046_remove_initiativerace_margin_win_loss'),
    ]

    operations = [
        migrations.AddField(
            model_name='initiativerace',
            name='show',
            field=models.BooleanField(default=False, help_text='Show the initiative race on the election results pages.'),
        ),
    ]
