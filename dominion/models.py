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

class Technique_Advantage(models.Model):
# table linking techniques with advantages between technique ID and advanage ID
	technique = models.ForeignKey(Technique)
	advantage = models.IntegerField()

class Technique_Sub_Advantage(models.Model):
#table linking a technique with an advantage where an optional advantage was chosen
#since django uses an auto id as the FK, and we have the technique in the Tech_Advantage table, we don't need to have it as a FK here
	advantage = models.ForeignKey(Technique_Advantage)
	sub_advantage = models.IntegerField()

class Technique_Disadvantage(models.Model):
#table linking a technique with the chosen disadvantages.
	technique = models.ForeignKey(Technique)
	#disadvantage is an integer corresponding to the ID of the disadvantage in the loaded JSON file
	disadvantage = models.IntegerField()