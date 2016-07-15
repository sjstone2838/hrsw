# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0010_auto_20160715_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='person',
            field=models.ForeignKey(to='ats.Person'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='project',
            field=models.ForeignKey(related_name='applicants', to='ats.Project'),
        ),
        migrations.AlterField(
            model_name='applicantevent',
            name='applicant',
            field=models.ForeignKey(related_name='applicantEvents', to='ats.Applicant'),
        ),
    ]
