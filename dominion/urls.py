from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt  
	
from . import views
	
urlpatterns = [
	# ex: /dominion/api/trees/1
	url(r'^api/trees/(?P<pk>[0-9]+)', views.SingleTree.as_view()),
	# ex: /dominion/api/trees/
	url(r'^api/trees/', views.AllTrees.as_view()),
	# ex: /dominion/api/techniques/1
	url(r'^api/techniques/(?P<pk>[0-9]+)', views.SingleTechnique.as_view()),
	# ex: /dominion/api/techniques/
	url(r'^api/techniques/', views.AllTechniques.as_view()),
	# ex: /dominion/api/disadvantages/1/levels/12
	url(r'^api/disadvantages/([0-9])/levels/(?P<pk>[0-9]+)', views.GetDisadvantageLevel.as_view()),
	# ex: /dominion/api/disadvantages/1/levels
	url(r'^api/disadvantages/(?P<pk>[0-9]+)/levels/', views.GetDisadvantageLevels.as_view()),
	# ex: /dominion/api/disadvantages/1/
	url(r'^api/disadvantages/(?P<pk>[0-9]+)', views.GetDisadvantage.as_view()),
	# ex: /dominion/api/disadvantages/
	url(r'^api/disadvantages/', views.GetDisadvantages.as_view()),
	# ex: /dominion/api/effects/1/modifiers/1/levels/12
	url(r'^api/effects/([0-9])/modifiers/([0-9])/levels/(?P<pk>[0-9]+)', views.GetEffectModifierLevel.as_view()),
	# ex: /dominion/api/effects/1/modifiers/1/levels
	url(r'^api/effects/([0-9])/modifiers/(?P<pk>[0-9]+)/levels/', views.GetEffectModifierLevels.as_view()),
	# ex: /dominion/api/effects/1/modifiers/1
	url(r'^api/effects/([0-9])/modifiers/(?P<pk>[0-9]+)', views.GetEffectModifier.as_view()),
	# ex: /dominion/api/ffects/1/modifiers/
	url(r'^api/effects/(?P<pk>[0-9])/modifiers', views.GetEffectModifiers.as_view()),
	# ex: /dominion/api/effects/1/levels/123  The effect number means nothing, but it makes sense to be consistent.
	url(r'^api/effects/([0-9])/levels/(?P<pk>[0-9]+)', views.GetEffectLevel.as_view()),
	# ex: /dominion/api/effects/1/levels/
	url(r'^api/effects/(?P<pk>[0-9]+)/levels/', views.GetEffectLevels.as_view()),
	# ex: /dominion/api/effects/1
	url(r'^api/effects/(?P<pk>[0-9]+)', views.GetEffect.as_view()),
	# ex: /dominion/api/effects/
	url(r'^api/effects/', views.GetEffects.as_view()),
]