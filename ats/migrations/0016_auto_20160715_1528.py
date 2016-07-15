# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0015_auto_20160715_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionset',
            name='applicantEvent',
        ),
        migrations.RemoveField(
            model_name='questionset',
            name='project',
        ),
        migrations.RemoveField(
            model_name='questionset',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='questionset',
            name='role',
        ),
        migrations.AddField(
            model_name='question',
            name='applicantEvent',
            field=models.ForeignKey(related_name='questionSet', blank=True, to='ats.ApplicantEvent', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='project',
            field=models.ForeignKey(related_name='questionSet', blank=True, to='ats.Project', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='role',
            field=models.ForeignKey(related_name='questionSet', blank=True, to='ats.Role', null=True),
        ),
        migrations.DeleteModel(
            name='QuestionSet',
        ),
    ]
