# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0022_auto_20160802_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 18, 42, 383567), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 18, 53, 177908), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicantevent',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 18, 57, 702801), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicantevent',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 19, 1, 9596), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 19, 5, 889754), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 19, 9, 626910), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 19, 13, 379683), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 19, 17, 23790), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 19, 21, 436458), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 19, 24, 769432), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='role',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 19, 29, 188364), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='role',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 19, 32, 589846), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 19, 36, 9976), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 9, 19, 39, 786143), auto_now=True),
            preserve_default=False,
        ),
    ]
