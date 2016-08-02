# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0018_auto_20160728_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicantevent',
            old_name='eventType',
            new_name='event_type',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='filledPositionsCount',
            new_name='filled_positions_count',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='openPositionsCount',
            new_name='open_positions_count',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='applicantEvent',
            new_name='applicant_event',
        ),
    ]
