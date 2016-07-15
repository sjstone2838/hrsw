# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0009_auto_20160715_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='person',
            field=models.ForeignKey(related_name='Applicant_Person', to='ats.Person'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='project',
            field=models.ForeignKey(related_name='Applicant_Project', to='ats.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='organization',
            field=models.ForeignKey(related_name='Project_Organization', to='ats.Organization'),
        ),
        migrations.AlterField(
            model_name='role',
            name='organization',
            field=models.ForeignKey(related_name='Role_Organization', to='ats.Organization'),
        ),
    ]
