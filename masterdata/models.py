from django.db import models


class BaseContent(models.Model):

    ACTIVE_CHOICES = ((0, 'Inactive'), (2, 'Active'),)
    active = models.PositiveIntegerField(choices=ACTIVE_CHOICES,
                                         default=2)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)

    #                                        BaseContent
    class Meta:
        abstract = True

    #                                        BaseContent
    def switch(self):
        self.active = {2: 0, 0: 2}[self.active]
        self.save()

    def __str__(self):
        return self.name


class Country(BaseContent):

    pass


class State(BaseContent):

    country = models.ForeignKey('Country')
