from django.conf.urls import patterns, url

urlpatterns = patterns('suscribe.apps.suscribers.views',
	url(r'^$', 'home', name = 'home'),
)