# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('Identification_Number', models.IntegerField(default=0)),
                ('Please_repeat_Identification_Number', models.CharField(default=b'', max_length=200, serialize=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VitaminData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vitamin_Name', models.CharField(max_length=50)),
                ('vitamin_Boolean', models.CharField(max_length=30)),
                ('vitamin_Amount', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to='ffq.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='identify',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Identify',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
