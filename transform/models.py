from __future__ import unicode_literals
from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class TransformPartyPage(Page):
    body = RichTextField()
    signup_embed_code = models.TextField(
        blank=True,
        null=True,
        help_text='Raw HTML embed code for signup form, etc.'
    )
    social_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('signup_embed_code'),
        FieldPanel('body'),
    ]
    parent_page_types = ['transform.TransformPartyIndexPage']
    promote_panels = Page.promote_panels + [
        ImageChooserPanel('social_image')
    ]
    subpage_types = []


class TransformPartyIndexPage(Page):
    parent_page_types = ['pages.IndexPage']
    subpage_types = ['transform.TransformPartyPage']
