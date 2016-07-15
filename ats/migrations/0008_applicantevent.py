# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ats', '0007_auto_20160715_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventType', models.CharField(max_length=200, choices=[(b'Interview', b'Interview'), (b'Resume_submission', b'Resume_submission')])),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(to='ats.Applicant')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
    ]
