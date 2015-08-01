# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0009_disadvantage_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disadvantage_Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(default='')),
                ('mk', models.IntegerField()),
                ('level', models.IntegerField()),
                ('disadvantage', models.ForeignKey(to='dominion.Disadvantage')),
            ],
        ),
        migrations.RemoveField(
            model_name='disadvantage_levels',
            name='disadvantage',
        ),
        migrations.DeleteModel(
            name='Disadvantage_Levels',
        ),
    ]
