# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominion', '0004_auto_20150718_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('effect_name', models.CharField(max_length=100)),
                ('effect_description', models.TextField(default='')),
                ('effect_frequency', models.CharField(max_length=20)),
                ('effect_action_type', models.CharField(max_length=20)),
                ('effect_str_cost', models.IntegerField()),
                ('effect_dex_cost', models.IntegerField()),
                ('effect_agi_cost', models.IntegerField()),
                ('effect_con_cost', models.IntegerField()),
                ('effect_pow_cost', models.IntegerField()),
                ('effect_will_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Effect_Level',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('level_name', models.CharField(max_length=20)),
                ('level_primary_cost', models.IntegerField()),
                ('level_secondary_cost', models.IntegerField()),
                ('level_mk', models.IntegerField()),
                ('level_maint', models.IntegerField()),
                ('level_mis', models.IntegerField()),
                ('level_grs', models.IntegerField()),
                ('level_tech_level', models.IntegerField()),
                ('effect', models.ForeignKey(to='dominion.Effect')),
            ],
        ),
        migrations.CreateModel(
            name='Effect_Modifier',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('modifier_name', models.CharField(max_length=20)),
                ('modifier_description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Effect_Modifier_Level',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('level_name', models.CharField(max_length=20)),
                ('level_description', models.TextField(default='')),
                ('level_cost', models.IntegerField()),
                ('level_mk', models.IntegerField()),
                ('level_maint', models.IntegerField()),
                ('level_mis', models.IntegerField()),
                ('level_grs', models.IntegerField()),
                ('effect_modifier', models.ForeignKey(to='dominion.Effect_Modifier')),
            ],
        ),
        migrations.CreateModel(
            name='Technique_Effect_Modifier_Link',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('effect', models.ForeignKey(to='dominion.Effect')),
                ('effect_level', models.ForeignKey(to='dominion.Effect_Level')),
                ('effect_modifier', models.ForeignKey(null=True, to='dominion.Effect_Modifier')),
                ('effect_modifier_level', models.ForeignKey(null=True, to='dominion.Effect_Modifier_Level')),
                ('technique', models.ForeignKey(to='dominion.Technique')),
            ],
        ),
        migrations.RemoveField(
            model_name='technique_advantage',
            name='technique',
        ),
        migrations.RemoveField(
            model_name='technique_disadvantage',
            name='technique',
        ),
        migrations.RemoveField(
            model_name='technique_sub_advantage',
            name='advantage',
        ),
        migrations.RemoveField(
            model_name='tree',
            name='num_of_techniques',
        ),
        migrations.RemoveField(
            model_name='tree',
            name='total_mk',
        ),
        migrations.DeleteModel(
            name='Technique_Advantage',
        ),
        migrations.DeleteModel(
            name='Technique_Disadvantage',
        ),
        migrations.DeleteModel(
            name='Technique_Sub_Advantage',
        ),
        migrations.AddField(
            model_name='technique',
            name='effects',
            field=models.ManyToManyField(to='dominion.Effect'),
        ),
    ]
