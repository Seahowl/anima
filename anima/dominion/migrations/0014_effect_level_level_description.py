# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0013_auto_20150811_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='effect_level',
            name='level_description',
            field=models.TextField(default='', blank=True),
        ),
    ]
