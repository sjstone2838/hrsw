# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0011_auto_20160715_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantevent',
            name='owner',
            field=models.ForeignKey(to='ats.UserProfile', blank=True),
        ),
    ]
