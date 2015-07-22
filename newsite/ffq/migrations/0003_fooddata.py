# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffq', '0002_auto_20150721_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food_name', models.CharField(max_length=100)),
                ('food_freq', models.CharField(max_length=50)),
                ('food_misc', models.CharField(max_length=50, null=True, blank=True)),
                ('user', models.ForeignKey(to='ffq.User')),
            ],
        ),
    ]
