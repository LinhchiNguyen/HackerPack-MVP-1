from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^demo/$', views.demo, name='demo'),
	url(r'^company/$', views.company, name='company'),
	url(r'^tutorials/$', views.tutorials, name='tutorials')
	# Add refs for:
	# - user login
]
