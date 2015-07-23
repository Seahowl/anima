from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt  
    
from . import views
    
urlpatterns = [
	# ex: /dominion/api/trees/1
    url(r'^api/trees/(?P<pk>[0-9]+)', views.SingleTree.as_view()),
    # ex: /dominion/api/trees/
    url(r'^api/trees/', csrf_exempt(views.GetTrees.as_view())),
    # ex: /dominion/api/techniques/
    url(r'^api/techniques/', views.GetTechniques.as_view()),
    
]