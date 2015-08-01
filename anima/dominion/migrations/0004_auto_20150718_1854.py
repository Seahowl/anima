# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0003_technique_tree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree_technique',
            name='technique',
        ),
        migrations.RemoveField(
            model_name='tree_technique',
            name='tree',
        ),
        migrations.RemoveField(
            model_name='technique',
            name='tree',
        ),
        migrations.AddField(
            model_name='tree',
            name='techniques',
            field=models.ManyToManyField(to='dominion.Technique'),
        ),
        migrations.DeleteModel(
            name='Tree_Technique',
        ),
    ]
