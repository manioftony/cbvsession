from django.conf.urls import patterns, url
from masterdata import views as v


urlpatterns = patterns(
    '',
    url(r'^country/list/$', v.CountryList.as_view(), name='country_list'),
)
