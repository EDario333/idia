from django.conf.urls import url 
from . import views
 
urlpatterns = [ 
	# url(r'^api/axis$', views.view_all),
	# url(r'^api/axis/(?P<pk>[0-9]+)$', views.view_one),
	url(r'^', views.view_all),
	url(r'^(?P<pk>[0-9]+)$', views.view_one),
]