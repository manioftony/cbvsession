from django.views import generic as g
from django.db.models import get_model
from django.http import HttpResponseRedirect


class ManageBase(object):

    @property
    def model(self):
        return get_model('masterdata', self.kwargs.get('model'))

    def get_form_class(self):

        self.fields = {
            'country': ('name', ), 'state': ('country', 'name', )
        }[self.kwargs.get('model')]
        return super(ManageBase, self).get_form_class()


class List(ManageBase, g.ListView):
    template_name = 'masterdata/list.html'


class FormBase(ManageBase):

    template_name = 'masterdata/add-edit.html'

    def get_success_url(self):
        return "/masterdata/%s/list/" % (
            self.kwargs.get('model'))


class Create(FormBase, g.CreateView):
    pass


class Update(FormBase, g.UpdateView):
    pass


class Delete(FormBase, g.DeleteView):

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class Status(Delete):

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.switch()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
