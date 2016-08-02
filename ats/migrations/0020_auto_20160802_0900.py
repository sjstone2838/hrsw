# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0019_auto_20160801_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 8, 59, 57, 363892), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 0, 14, 777093), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicantevent',
            name='applicant',
            field=models.ForeignKey(related_name='applicant_events', to='ats.Applicant'),
        ),
    ]
