# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-02-06 00:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
        ('pages', '0056_auto_20180131_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberNewsletterPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header', wagtail.wagtailcore.fields.RichTextField()),
                ('body', wagtail.wagtailcore.fields.StreamField([('white_background', wagtail.wagtailcore.blocks.RichTextBlock()), ('blue_background', wagtail.wagtailcore.blocks.RichTextBlock()), ('image_block', wagtail.wagtailcore.blocks.StructBlock([('header', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
