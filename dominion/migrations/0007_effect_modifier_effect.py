# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0006_auto_20150720_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='effect_modifier',
            name='effect',
            field=models.ForeignKey(default=1, to='dominion.Effect'),
            preserve_default=False,
        ),
    ]
