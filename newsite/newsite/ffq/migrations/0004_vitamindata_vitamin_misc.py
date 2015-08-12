# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffq', '0003_fooddata'),
    ]

    operations = [
        migrations.AddField(
            model_name='vitamindata',
            name='vitamin_misc',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
