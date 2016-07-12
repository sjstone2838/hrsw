# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0002_auto_20160712_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='positionCount',
            new_name='openPositionsCount',
        ),
    ]
