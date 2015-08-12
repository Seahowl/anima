# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0012_auto_20150725_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='effect',
            name='effect_elements',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='effect',
            name='effect_level_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='effect_modifier',
            name='modifier_level_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
