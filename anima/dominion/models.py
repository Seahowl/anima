from django.db import models

# Create your models here.
class Effect(models.Model):
	effect_name = models.CharField(max_length=100)
	effect_description = models.TextField(default="")
	effect_frequency = models.CharField(max_length=20)
	effect_action_type = models.CharField(max_length=20)
	effect_level_name = models.CharField(max_length=20)
	effect_elements = models.CharField(max_length=50)
	#negative cost means the effect can't use that characteristic
	#zero cost means the effect uses that as it's default characteristic
	#positive cost adds to the effect's cost if the ki is split that direction.
	effect_str_cost = models.IntegerField()
	effect_dex_cost = models.IntegerField()
	effect_agi_cost = models.IntegerField()
	effect_con_cost = models.IntegerField()
	effect_pow_cost = models.IntegerField()
	effect_will_cost = models.IntegerField()

	def __str__(self):
		return self.effect_name	

class Effect_Modifier(models.Model):
	effect = models.ForeignKey(Effect)
	modifier_name = models.CharField(max_length=20)
	modifier_level_name = models.CharField(max_length=20)
	modifier_description = models.TextField(default="")

	def __str__(self):
		return str(self.effect) + " " + self.modifier_name	

class Effect_Modifier_Level(models.Model):
	effect_modifier = models.ForeignKey(Effect_Modifier)
	level_name = models.CharField(max_length=20)
	level_description = models.TextField(default="", blank=True)
	level_cost = models.IntegerField()
	level_mk = models.IntegerField()
	level_maint = models.IntegerField()
	level_mis = models.IntegerField()
	level_grs = models.IntegerField()

	def __str__(self):
		return str(self.effect_modifier) + " " + self.level_name	

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

	def __str__(self):
		return str(self.effect) + " " + self.level_name	

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
	effect_levels = models.ManyToManyField(Effect_Level)
	effect_modifiers = models.ManyToManyField(Effect_Modifier, blank=True)
	effects_modifier_levels = models.ManyToManyField(Effect_Modifier_Level, blank=True)
	def __str__(self):
		return self.name	

class Tree(models.Model):
# a Tree has it's own attributes, and is made up of many techniques (Tree_Technique)
	name = models.CharField(max_length=200)
	description = models.TextField(default="")
	techniques = models.ManyToManyField(Technique)

	def __str__(self):
		return self.name

class Disadvantage(models.Model):
	name = models.CharField(max_length=20)
	description	= models.TextField(default="")
	action = models.CharField(max_length=40)

	def __str__(self):
		return self.name

class Disadvantage_Level(models.Model):
	disadvantage = models.ForeignKey(Disadvantage)
	name = models.CharField(max_length=40)
	description = models.TextField(default="", blank=True)
	mk = models.IntegerField()
	level = models.IntegerField()

	def __str__(self):
		return str(self.disadvantage) + " " + self.name