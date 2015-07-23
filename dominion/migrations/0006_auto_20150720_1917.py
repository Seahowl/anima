# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0005_auto_20150719_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technique_effect_modifier_link',
            name='effect',
        ),
        migrations.RemoveField(
            model_name='technique_effect_modifier_link',
            name='effect_level',
        ),
        migrations.RemoveField(
            model_name='technique_effect_modifier_link',
            name='effect_modifier',
        ),
        migrations.RemoveField(
            model_name='technique_effect_modifier_link',
            name='effect_modifier_level',
        ),
        migrations.RemoveField(
            model_name='technique_effect_modifier_link',
            name='technique',
        ),
        migrations.AddField(
            model_name='technique',
            name='effect_levels',
            field=models.ManyToManyField(to='dominion.Effect_Level'),
        ),
        migrations.AddField(
            model_name='technique',
            name='effect_modifiers',
            field=models.ManyToManyField(to='dominion.Effect_Modifier'),
        ),
        migrations.AddField(
            model_name='technique',
            name='effects_modifier_levels',
            field=models.ManyToManyField(to='dominion.Effect_Modifier_Level'),
        ),
        migrations.DeleteModel(
            name='Technique_Effect_Modifier_Link',
        ),
    ]
