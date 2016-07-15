# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0013_auto_20160715_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionset',
            name='applicantEvent',
            field=models.ForeignKey(related_name='questionSet', blank=True, to='ats.ApplicantEvent', null=True),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='project',
            field=models.ForeignKey(related_name='questionSet', blank=True, to='ats.Project', null=True),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='role',
            field=models.ForeignKey(related_name='questionSet', blank=True, to='ats.Role', null=True),
        ),
    ]
