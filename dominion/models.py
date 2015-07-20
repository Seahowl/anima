from django.db import models

# Create your models here.

class Technique(models.Model):
# a Technique has its own attributes, and has advantages (which might have their own advantages) and disadvantages
	name = models.CharField(max_length=200)
	level = models.IntegerField()
	mk = models.IntegerField()
	description = models.TextField()
	technique_type = models.CharField(max_length=20)
	#for an additional cost, the user can spread cost around to certain attributes
	#same with the maintainence cost as well
	#so we need to save the cost and maintance on a technique level
	str_cost = models.IntegerField()
	str_maint = models.IntegerField()
	dex_cost = models.IntegerField()
	dex_maint = models.IntegerField()
	agi_cost = models.IntegerField()
	agi_maint = models.IntegerField()
	con_cost = models.IntegerField()
	con_maint = models.IntegerField()
	pow_cost = models.IntegerField()
	pow_maint = models.IntegerField()
	will_cost = models.IntegerField()
	will_maint = models.IntegerField()
	#the advantages/disadvantages are saved in related tables, so we don't need any room for them here
	def __str__(self):
		return self.name	

class Tree(models.Model):
# a Tree has it's own attributes, and is made up of many techniques (Tree_Technique)
	name = models.CharField(max_length=200)
	description = models.TextField(default="")
	techniques = models.ManyToManyField(Technique)

	def __str__(self):
		return self.name	

class Effect(models.Model):
	effect_name = models.CharField(max_length=100)
	effect_description = models.TextField(default="")
	effect_frequency = models.d

class Effect_Level(models.Model):
	effect = models.ForeignKey(Effect)
	level_name = models.CharField(max_length=20)
	level_primary_cost = models.IntegerField()
	level_secondary_cost = models.IntegerField()
	level_mk = models.IntegerField()
	level_maint = models.IntegerField()
	level_mis = models.IntegerField()
	level_grs = models.IntegerField()
	level_tech_level = models.IntegerField()

class Effect_Modifier(models.Model):
	modifier_name = models.CharField(max_length=20)
	modifier_description = models.TextField(default="")
	effect_modifier_levels = models.ForeignKey(Effect_Modifier_Level)

class Effect_Modifier_Level(models.Model):
	effect_modifier = models.ForeignKey(Effect_Modifier)
	level_name = models.CharField(max_length=20)
	level_description = models.TextField(default="")
	level_cost = models.IntegerField()
	level_mk = models.IntegerField()
	level_maint = models.IntegerField()
	level_mis = models.IntegerField()
	level_grs = models.IntegerField()
