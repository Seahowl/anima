from django.contrib import admin

# Register your models here.
from .models import Tree, Technique, Effect, Effect_Level, Effect_Modifier, Effect_Modifier_Level, Disadvantage, Disadvantage_Level

admin.site.register(Tree)
admin.site.register(Technique)
admin.site.register(Effect)
admin.site.register(Effect_Level)
admin.site.register(Effect_Modifier)
admin.site.register(Effect_Modifier_Level)
admin.site.register(Disadvantage)
admin.site.register(Disadvantage_Level)