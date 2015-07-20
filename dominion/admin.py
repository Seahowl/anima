from django.contrib import admin

# Register your models here.
from .models import Tree, Technique

admin.site.register(Tree)
admin.site.register(Technique)