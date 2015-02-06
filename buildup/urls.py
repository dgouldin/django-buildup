from django.conf.urls import patterns, url
urlpatterns = patterns('', url(r'^$', 'buildup.views.hello', name='hello'))
