from django.conf.urls import patterns, url
from masterdata import views as v


urlpatterns = patterns(
    '',
    url(r'^(?P<model>(:?country|state))/list/$', v.List.as_view(), name='list'),
)
