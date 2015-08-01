# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0010_auto_20150725_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disadvantage_level',
            name='description',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='effect_modifier_level',
            name='level_description',
            field=models.TextField(default='', blank=True),
        ),
    ]
