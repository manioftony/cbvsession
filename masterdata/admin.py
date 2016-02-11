from django.contrib import admin
register = admin.site.register
from .models import Country, State


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', )


class StateAdmin(admin.ModelAdmin):
    list_display = ('country', 'name', 'active', )


register(Country, CountryAdmin)
register(State, StateAdmin)
