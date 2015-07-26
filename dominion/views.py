from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.core import serializers
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from .models import Tree, Technique, Effect, Effect_Level, Effect_Modifier, Effect_Modifier_Level, Disadvantage, Disadvantage_Levels
# Create your views here.
class AllTrees(View):
	def get(self, request):
		serializedTrees = serializers.serialize("json", Tree.objects.all())
		return HttpResponse(serializedTrees, content_type="application/json")
	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

#No get here because it's a full get/post/delete method
class SingleTree(View):
	def get(self, request, pk):
		serializedTree = serializers.serialize("json", Tree.objects.filter(pk=self.kwargs['pk']))
		#commented out right now, we're 
		#techniqueLocation = serializedTree.find('"techniques": ')
		#techniqueStart = serializedTree.find('[', techniqueLocation)
		#techniqueEnd = serializedTree.find(']', techniqueLocation)
		#serializedTechniques = serializers.serialize("json", Technique.objects.filter(tree__pk=self.kwargs['pk']))
		#serializedTree = serializedTree.replace(serializedTree[techniqueStart:techniqueEnd+1], serializedTechniques)
		return HttpResponse(serializedTree, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

#this is the technique post/get all
class AllTechniques(View):
	def get(self, request):
		serializedTechniques = serializers.serialize("json", Technique.objects.all())
		return HttpResponse(serializedTechniques, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

#this is the technique put/delete/get
class SingleTechnique(View):
	def get(self, request, pk):
		technique = Technique.objects.filter(pk=self.kwargs['pk'])
		serializedTechnique = serializers.serialize("json", technique)
		return HttpResponse(serializedTechnique, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetEffects(View):
	def get(self, request):
		serializedEffects = serializers.serialize("json", Effect.objects.all())
		return HttpResponse(serializedEffects, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetEffect(View):
	def get(self, request, pk):
		serializedEffects = serializers.serialize("json", Effect.objects.filter(pk=self.kwargs['pk']))
		return HttpResponse(serializedEffects, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetEffectLevels(View):
	def get(self, request, pk):
		serializedEffects = serializers.serialize("json", Effect_Level.objects.filter(effect=self.kwargs['pk']))
		return HttpResponse(serializedEffects, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetEffectLevel(View):
	def get(self, request, pk):
		serializedEffects = serializers.serialize("json", Effect_Level.objects.filter(pk=self.kwargs['pk']))
		return HttpResponse(serializedEffects, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetEffectModifiers(View):
	def get(self, request, pk):
		serializedEffects = serializers.serialize("json", Effect_Modifier.objects.filter(effect=self.kwargs['pk']))
		return HttpResponse(serializedEffects, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetEffectModifier(View):
	def get(self, request, pk):
		serializedEffects = serializers.serialize("json", Effect_Modifier.objects.filter(pk=self.kwargs['pk']))
		return HttpResponse(serializedEffects, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetEffectModifierLevels(View):
	def get(self, request, pk):
		serializedEffects = serializers.serialize("json", Effect_Modifier_Level.objects.filter(effect_modifier=self.kwargs['pk']))
		return HttpResponse(serializedEffects, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetEffectModifierLevel(View):
	def get(self, request, pk):
		serializedEffects = serializers.serialize("json", Effect_Modifier_Level.objects.filter(pk=self.kwargs['pk']))
		return HttpResponse(serializedEffects, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetDisadvantages(View):
	def get(self, request):
		serializedDisadvantages = serializers.serialize("json", Disadvantage.objects.all())
		return HttpResponse(serializedDisadvantages, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetDisadvantage(View):
	def get(self, request, pk):
		serializedEffects = serializers.serialize("json", Disadvantage.objects.filter(pk=self.kwargs['pk']))
		return HttpResponse(serializedEffects, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetDisadvantageLevels(View):
	def get(self, request, pk):
		serializedEffects = serializers.serialize("json", Disadvantage_Levels.objects.filter(disadvantage=self.kwargs['pk']))
		return HttpResponse(serializedEffects, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])

class GetDisadvantageLevel(View):
	def get(self, request, pk):
		serializedEffects = serializers.serialize("json", Disadvantage_Levels.objects.filter(pk=self.kwargs['pk']))
		return HttpResponse(serializedEffects, content_type="application/json")

	def put(self, request):
		return HttpResponseNotAllowed(['GET'])
	def post(self, request):
		return HttpResponseNotAllowed(['GET'])
	def delete(self, request):
		return HttpResponseNotAllowed(['GET'])