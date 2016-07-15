# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0008_applicantevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantevent',
            name='datetime',
            field=models.DateTimeField(blank=True),
        ),
    ]
