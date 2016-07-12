# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0003_auto_20160712_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='filledPositionsCount',
            field=models.IntegerField(default=0),
        ),
    ]
