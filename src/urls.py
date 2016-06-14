from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^company/$', views.company, name='company'),
	# Add refs for:
	# - user login
	# - tutorials
]
