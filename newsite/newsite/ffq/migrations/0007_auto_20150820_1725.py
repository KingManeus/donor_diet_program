# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffq', '0006_questiondata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vitamindata',
            old_name='vitamin_misc',
            new_name='vitamin_Dose',
        ),
        migrations.RemoveField(
            model_name='vitamindata',
            name='vitamin_Amount',
        ),
        migrations.RemoveField(
            model_name='vitamindata',
            name='vitamin_Boolean',
        ),
        migrations.AddField(
            model_name='vitamindata',
            name='vitamin_Freq',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vitamindata',
            name='vitamin_Name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
