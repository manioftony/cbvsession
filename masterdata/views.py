from django.views.generic import ListView
from django.db.models import get_model


class List(ListView):

    @property
    def model(self):
        return get_model('masterdata', self.kwargs.get('model'))

    template_name = 'masterdata/list.html'
