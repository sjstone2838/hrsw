# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0014_auto_20160715_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='applicantEvent',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='index',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
