from django.conf.urls import patterns, include, url
from django.contrib import admin
from masterdata import urls as masterdata


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^masterdata/', include(masterdata)),
)
