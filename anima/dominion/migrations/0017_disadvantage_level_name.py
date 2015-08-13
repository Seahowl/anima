# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0016_auto_20150812_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='disadvantage',
            name='level_name',
            field=models.CharField(default='Loss of Fatigue', max_length=40),
            preserve_default=False,
        ),
    ]
