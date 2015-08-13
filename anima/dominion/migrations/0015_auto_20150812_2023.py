# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0014_effect_level_level_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='mk',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tree',
            name='num_techniques',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
