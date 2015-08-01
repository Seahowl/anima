# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level', models.IntegerField()),
                ('mk', models.IntegerField()),
                ('description', models.TextField()),
                ('technique_type', models.CharField(max_length=20)),
                ('str_cost', models.IntegerField()),
                ('str_maint', models.IntegerField()),
                ('dex_cost', models.IntegerField()),
                ('dex_maint', models.IntegerField()),
                ('agi_cost', models.IntegerField()),
                ('agi_maint', models.IntegerField()),
                ('con_cost', models.IntegerField()),
                ('con_maint', models.IntegerField()),
                ('pow_cost', models.IntegerField()),
                ('pow_maint', models.IntegerField()),
                ('will_cost', models.IntegerField()),
                ('will_maint', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Technique_Advantage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('advantage', models.IntegerField()),
                ('technique', models.ForeignKey(to='dominion.Technique')),
            ],
        ),
        migrations.CreateModel(
            name='Technique_Disadvantage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('disadvantage', models.IntegerField()),
                ('technique', models.ForeignKey(to='dominion.Technique')),
            ],
        ),
        migrations.CreateModel(
            name='Technique_Sub_Advantage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sub_advantage', models.IntegerField()),
                ('advantage', models.ForeignKey(to='dominion.Technique_Advantage')),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tree_Technique',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('technique', models.ForeignKey(to='dominion.Technique')),
                ('tree', models.ForeignKey(to='dominion.Tree')),
            ],
        ),
    ]
