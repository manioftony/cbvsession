from django.conf.urls import patterns, url
from masterdata import views as v


urlpatterns = patterns(
    '',
    url(r'^(?P<model>(:?country|state))/list/$', v.List.as_view(), name='list'),
    url(r'^(?P<model>(:?country|state))/create/$', v.Create.as_view(), name='create'),
    url(r'^(?P<model>(:?country|state))/update/(?P<pk>\d+)/$', v.Update.as_view(), name='update'),
)
