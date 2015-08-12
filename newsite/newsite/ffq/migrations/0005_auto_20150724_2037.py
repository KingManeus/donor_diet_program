# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffq', '0004_vitamindata_vitamin_misc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitamindata',
            name='vitamin_misc',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
