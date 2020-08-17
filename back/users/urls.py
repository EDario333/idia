from django.conf.urls import url 
from . import views

urlpatterns = [ 
	url(r'login$', views.login),
	url(r'^', views.view_all),
	url(r'^(?P<pk>[0-9]+)$', views.view_one),
]