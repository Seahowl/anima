# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0011_auto_20150725_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technique',
            name='effect_modifiers',
            field=models.ManyToManyField(to='dominion.Effect_Modifier', blank=True),
        ),
        migrations.AlterField(
            model_name='technique',
            name='effects_modifier_levels',
            field=models.ManyToManyField(to='dominion.Effect_Modifier_Level', blank=True),
        ),
    ]
