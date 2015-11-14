from django.conf.urls import patterns, url

urlpatterns = patterns('apps.suscribers.views',
	url(r'^$', 'home', name = 'home'),
)