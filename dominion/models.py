from django.db import models

# Create your models here.
class Effect(models.Model):
	effect_name = models.CharField(max_length=100)
	effect_description = models.TextField(default="")
	effect_frequency = models.CharField(max_length=20)
	effect_action_type = models.CharField(max_length=20)
	#negative cost means the effect can't use that characteristic
	#zero cost means the effect uses that as it's default characteristic
	#positive cost adds to the effect's cost if the ki is split that direction.
	effect_str_cost = models.IntegerField()
	effect_dex_cost = models.IntegerField()
	effect_agi_cost = models.IntegerField()
	effect_con_cost = models.IntegerField()
	effect_pow_cost = models.IntegerField()
	effect_will_cost = models.IntegerField()

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
	effects = models.ManyToManyField(Effect)
	def __str__(self):
		return self.name	

class Tree(models.Model):
# a Tree has it's own attributes, and is made up of many techniques (Tree_Technique)
	name = models.CharField(max_length=200)
	description = models.TextField(default="")
	techniques = models.ManyToManyField(Technique)

	def __str__(self):
		return self.name	

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

class Effect_Modifier_Level(models.Model):
	effect_modifier = models.ForeignKey(Effect_Modifier)
	level_name = models.CharField(max_length=20)
	level_description = models.TextField(default="")
	level_cost = models.IntegerField()
	level_mk = models.IntegerField()
	level_maint = models.IntegerField()
	level_mis = models.IntegerField()
	level_grs = models.IntegerField()

class Technique_Effect_Modifier_Link(models.Model):
	technique = models.ForeignKey(Technique)
	effect = models.ForeignKey(Effect)
	effect_level = models.ForeignKey(Effect_Level)
	effect_modifier = models.ForeignKey(Effect_Modifier, null=True)
	effect_modifier_level = models.ForeignKey(Effect_Modifier_Level, null=True)
