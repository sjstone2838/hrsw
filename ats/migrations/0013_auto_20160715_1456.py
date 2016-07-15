# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0012_auto_20160715_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField(default=b'', blank=True)),
                ('applicantEvent', models.ForeignKey(to='ats.ApplicantEvent')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(default=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('applicantEvent', models.ForeignKey(related_name='questionSet', blank=True, to='ats.ApplicantEvent')),
                ('project', models.ForeignKey(related_name='questionSet', blank=True, to='ats.Project')),
                ('questions', models.ManyToManyField(to='ats.Question', blank=True)),
                ('role', models.ForeignKey(related_name='questionSet', blank=True, to='ats.Role')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='ats.Question'),
        ),
    ]
