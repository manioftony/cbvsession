from django.views import generic as g
from django.db.models import get_model


class List(g.ListView):

    @property
    def model(self):
        return get_model('masterdata', self.kwargs.get('model'))

    template_name = 'masterdata/list.html'


class Create(g.CreateView):

    @property
    def model(self):
        return get_model('masterdata', self.kwargs.get('model'))

    template_name = 'masterdata/add-edit.html'

    def get_success_url(self):
        return "/masterdata/%s/list/" % (
            self.kwargs.get('model'))
