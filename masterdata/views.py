from django.views import generic as g
from django.db.models import get_model


class ManageBase(object):

    @property
    def model(self):
        return get_model('masterdata', self.kwargs.get('model'))


class List(ManageBase, g.ListView):

    template_name = 'masterdata/list.html'


class Create(ManageBase, g.CreateView):

    template_name = 'masterdata/add-edit.html'

    def get_success_url(self):
        return "/masterdata/%s/list/" % (
            self.kwargs.get('model'))
