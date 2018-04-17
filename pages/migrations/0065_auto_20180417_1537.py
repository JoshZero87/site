# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-04-17 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0064_membernewsletterpage_share_copy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membernewsletterpage',
            name='share_copy',
            field=models.CharField(blank=True, help_text='\n            Copy that will be included in social posts when the share\n            buttons at the bottom of the email are used.', max_length=256, null=True),
        ),
    ]
