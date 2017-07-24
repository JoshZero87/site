# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 23:11
from __future__ import unicode_literals

from bs4 import BeautifulSoup
from django.contrib.contenttypes.models import ContentType
from django.db import migrations
from django.template.defaultfilters import slugify, yesno
from wagtail.wagtailcore.models import Page
import requests


def populate_candidate_pages(apps, schema_edtior):
    from pages.models import CandidateEndorsementIndexPage, CandidateEndorsementPage
    from endorsements.models import Candidate
    # CandidateEndorsementPage = apps.get_model('pages', 'CandidateEndorsementPage')
    # Candidate = apps.get_model('endorsements', 'Candidate')

    candidate_root_page = CandidateEndorsementIndexPage.objects.get(title='Our Candidates')

    for candidate in Candidate.objects.all():
        req = requests.get("http://ourrevolution.com/candidates/%s" % candidate.slug)
        try:
            html_content = BeautifulSoup(req.text, "html5lib").select('p.candidate-bio')[0].contents[0].strip()
            signup_tagline = BeautifulSoup(req.text, "html5lib").select('h3')[0].text.strip()
        except BaseException, e:
            print "Failed on %s: %s" % (req.url, e.message)
            continue

        page = CandidateEndorsementPage(**{
                'title': candidate.name,
                'slug': candidate.slug,
                'body': html_content,
                'candidate': candidate,
                'signup_tagline': signup_tagline
                # 'content_type': ContentType.objects.get_for_model(CandidateEndorsementPage),
            })

        candidate_root_page.add_child(instance=page)
        


def truncate_candidate_pages(apps, schema_edtior):
    CandidateEndorsementPage = apps.get_model('pages', 'CandidateEndorsementPage')
    CandidateEndorsementPage.objects.all().delete()


def populate_initiative_pages(apps, schema_edtior):
    from pages.models import InitiativeEndorsementIndexPage, InitiativeEndorsementPage
    from endorsements.models import Initiative

    initiative_root_page = InitiativeEndorsementIndexPage.objects.get(title='Our Initiatives')

    for initiative in Initiative.objects.all():
        req = requests.get("http://ourrevolution.com/ballot-initiatives/%s" % initiative.slug)
        try:
            html_content = BeautifulSoup(req.text, "html5lib").select('p.candidate-bio')[0].contents[0].strip()
            signup_tagline = BeautifulSoup(req.text, "html5lib").select('h3')[0].text.strip()
        except BaseException, e:
            print "Failed on %s: %s" % (req.url, e.message)
            continue

        page_title = "%s on %s %s: %s" % (yesno(initiative.vote).title(), initiative.state, initiative.title, initiative.name)

        page = InitiativeEndorsementPage(**{
                'title': page_title,
                'slug': initiative.slug,
                'body': html_content,
                'initiative': initiative,
                'signup_tagline': signup_tagline
                # 'content_type': ContentType.objects.get_for_model(CandidateEndorsementPage),
            })

        initiative_root_page.add_child(instance=page)


def truncate_initiative_pages(apps, schema_edtior):
    InitiativeEndorsementPage = apps.get_model('pages', 'InitiativeEndorsementPage')
    InitiativeEndorsementPage.objects.all().delete()


def populate_issue_pages(apps, schema_edtior):
    from pages.models import IssueIndexPage, IssuePage
    from endorsements.models import Issue

    issue_root_page = IssueIndexPage.objects.get(title='Our Issues')

    for issue in Issue.objects.all():
        req = requests.get("http://ourrevolution.com/issues/%s" % issue.slug)
        try:
            html_content = BeautifulSoup(req.text, "html5lib").select('.issues__content')[0]
            signup_tagline = html_content.select('.sign-up-form h3')[0].text.strip()
            [form.extract() for form in html_content.select('.sign-up-form')]
            html_content = "\n".join([unicode(c).strip() for c in html_content])
        except BaseException, e:
            print "Failed on %s: %s" % (req.url, e.message)
            continue

        page = IssuePage(**{
                'title': issue.name,
                'body': html_content,
                'issue': issue,
                'signup_tagline': signup_tagline
                # 'content_type': ContentType.objects.get_for_model(CandidatePage),
            })

        issue_root_page.add_child(instance=page)


def truncate_issue_pages(apps, schema_edtior):
    IssuePage = apps.get_model('pages', 'IssuePage')
    IssuePage.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_bootstrap_wagtail_site'),
    ]

    operations = [
        migrations.RunPython(populate_candidate_pages, reverse_code=truncate_candidate_pages),
        migrations.RunPython(populate_initiative_pages, reverse_code=truncate_initiative_pages),
        migrations.RunPython(populate_issue_pages, reverse_code=truncate_issue_pages)
    ]
