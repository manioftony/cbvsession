from django.views.generic import ListView
from .models import Country, State


class CountryList(ListView):

    model = Country
    template_name = 'masterdata/list.html'
