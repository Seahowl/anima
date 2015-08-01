# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='tree',
            name='num_of_techniques',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tree',
            name='total_mk',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
