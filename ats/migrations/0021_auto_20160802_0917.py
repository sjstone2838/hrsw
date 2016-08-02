# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0020_auto_20160802_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='created',
        ),
        migrations.AlterField(
            model_name='project',
            name='organization',
            field=models.ForeignKey(to='ats.Organization'),
        ),
        migrations.AlterField(
            model_name='project',
            name='role',
            field=models.ForeignKey(to='ats.Role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='organization',
            field=models.ForeignKey(to='ats.Organization'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='organization',
            field=models.ForeignKey(to='ats.Organization'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
