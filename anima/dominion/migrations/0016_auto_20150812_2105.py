# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0015_auto_20150812_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='technique',
            name='disadvantages',
            field=models.ManyToManyField(blank=True, to='dominion.Disadvantage'),
        ),
        migrations.AddField(
            model_name='technique',
            name='disadvantages_levels',
            field=models.ManyToManyField(blank=True, to='dominion.Disadvantage_Level'),
        ),
    ]
