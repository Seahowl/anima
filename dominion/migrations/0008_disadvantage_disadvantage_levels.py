# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0007_effect_modifier_effect'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disadvantage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Disadvantage_Levels',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(default='')),
                ('mk', models.IntegerField()),
                ('level', models.IntegerField()),
                ('disadvantage', models.ForeignKey(to='dominion.Disadvantage')),
            ],
        ),
    ]
