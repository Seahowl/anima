from django.contrib import admin

# Register your models here.
from .models import Tree, Technique

class TreeAdmin(admin.ModelAdmin):
      list_display = ['name', 'total_mk', 'num_of_techniques']

admin.site.register(Tree, TreeAdmin)
admin.site.register(Technique)
admin.site.register(Technique_Advantage)
admin.site.register(Technique_Disadvantage)
admin.site.register(Technique_Sub_Advantage)