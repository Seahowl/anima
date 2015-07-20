from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.generic import View

from .models import Tree, Technique
# Create your views here.

class GetTrees(View):
	def get(self, request):
		serializedTrees = serializers.serialize("json", Tree.objects.all())

		return HttpResponse(serializedTrees, content_type="application/json")

def GetUserTrees():
	return JsonResponse(Tree.objects.all(), safe=False)

#No get here because it's a full get/post/delete method
class SingleTree(View):
	def get(self, request, pk):
		tree = Tree.objects.filter(pk=self.kwargs['pk'])
		serializedTree = serializers.serialize("json", tree)
		techniqueLocation = serializedTree.find('"techniques": ')
		techniqueStart = serializedTree.find('[', techniqueLocation)
		techniqueEnd = serializedTree.find(']', techniqueLocation)
		serializedTechniques = serializers.serialize("json", Technique.objects.filter(tree__pk=self.kwargs['pk']))
		serializedTree = serializedTree.replace(serializedTree[techniqueStart:techniqueEnd+1], serializedTechniques)
		return HttpResponse(serializedTree, content_type="application/json")
#str(techniqueLocation) + " " + str(techniqueStart) + " " + str(techniqueEnd)
class GetTechniques(View):
	def get(self, request):
		serializedTechniques = serializers.serialize("json", Technique.objects.all())

		return HttpResponse(serializedTechniques, content_type="application/json")

def GetUserTechniques():
	return JsonResponse(Tree.objects.all(), safe=False)
#No get here because it's a full get/post/delete method
def SingleTechnique():
	return JsonResponse(Tree.objects.all(), safe=False)
def GetAdvantages():
	return JsonResponse(Tree.objects.all(), safe=False)
def GetAdvantage():
	return JsonResponse(Tree.objects.all(), safe=False)
def GetDisadvantages():
	return JsonResponse(Tree.objects.all(), safe=False)
def GetDisadvantage():
	return JsonResponse(Tree.objects.all(), safe=False)