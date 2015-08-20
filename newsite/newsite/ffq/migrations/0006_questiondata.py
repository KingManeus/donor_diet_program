# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffq', '0005_auto_20150724_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionData',
            fields=[
                ('field_number', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('field_answer', models.CharField(max_length=100, null=True, blank=True)),
                ('user', models.ForeignKey(to='ffq.User')),
            ],
        ),
    ]
