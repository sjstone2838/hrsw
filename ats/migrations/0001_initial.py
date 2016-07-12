# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('industry', models.CharField(default=b'', max_length=200, blank=True, choices=[(b'Retail', b'Retail'), (b'Software', b'Software'), (b'Hardware', b'Hardware'), (b'Healthcare', b'Healthcare'), (b'Industrial', b'Industrial'), (b'Hospitality', b'Hospitality')])),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default=b'', max_length=1000, blank=True, choices=[(b'Pre-launch', b'Pre-launch'), (b'Active', b'Active'), (b'Paused', b'Paused'), (b'Closed', b'Closed')])),
                ('positionCount', models.IntegerField(default=0, null=True, blank=True)),
                ('organization', models.ForeignKey(related_name='Role_Organization', to='ats.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default=b'', max_length=200)),
                ('description', models.TextField(default=b'', blank=True)),
                ('organization', models.ForeignKey(related_name='Project_Organization', to='ats.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.ForeignKey(related_name='UserProfile_Organization', to='ats.Organization')),
                ('user', models.ForeignKey(related_name='UserProfile_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='role',
            field=models.ForeignKey(related_name='Role', to='ats.Role'),
        ),
    ]
