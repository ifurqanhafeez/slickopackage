
from django.urls import path, include 
from django.conf.urls import url

from . import views

urlpatterns = [
	path('', views.home),
	path('home/', views.home),
	path('about/', views.about),
	path('package/', views.package),
	path('industry/', views.industry),
	path('whyus/', views.whyus),
	path('category/', views.category),
	path('terms/', views.terms),
	path('industrycategory/', views.industrycategory),
	path('contact/', views.snippet_detail),
	path('quote/', views.snippet_quote),
	url(r'^iitem/(?P<itemid>[0-9]+)', views.iitem, name='iitem'),
	url(r'^pitem/(?P<itemid>[0-9]+)', views.pitem, name='pitem'),
	url(r'^sitem/(?P<itemid>[0-9]+)', views.sitem, name='sitem'),
 

#	url(r'^$', views.home)
#	url(r'^$', views.about),
#	url(r'^$', views.contact),
#	url(r'^$', views.index)
]