# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0002_auto_20150716_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='technique',
            name='tree',
            field=models.ManyToManyField(to='dominion.Tree'),
        ),
    ]
