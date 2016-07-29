# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0016_auto_20160715_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='applicantEvent',
            field=models.ForeignKey(related_name='questions', blank=True, to='ats.ApplicantEvent', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='project',
            field=models.ForeignKey(related_name='questions', blank=True, to='ats.Project', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='role',
            field=models.ForeignKey(related_name='questions', blank=True, to='ats.Role', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(related_name='UserProfile_User', to=settings.AUTH_USER_MODEL),
        ),
    ]
