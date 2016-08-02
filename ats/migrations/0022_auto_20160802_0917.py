# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0021_auto_20160802_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created',
        ),
        migrations.RemoveField(
            model_name='role',
            name='created',
        ),
    ]
