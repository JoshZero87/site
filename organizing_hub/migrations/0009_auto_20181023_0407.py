# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-23 04:07
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizing_hub', '0008_auto_20181016_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizinghubdashboardpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('link_block', wagtail.wagtailcore.blocks.StructBlock([('text', wagtail.wagtailcore.blocks.TextBlock()), ('url', wagtail.wagtailcore.blocks.URLBlock()), ('feature_access_required', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, 'Calling Tool')], help_text='\n                Select Feature if access should be restricted only to local\n                groups that have this Feature enabled.\n                ', required=False))]))]),
        ),
    ]
