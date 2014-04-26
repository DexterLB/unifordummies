from django.shortcuts import render
from django.views.generic import ListView


from default import models


class ProgrammeListView(ListView):
    model = models.Programme
    templates = 'default/programme_list'
    context_object_name = 'programmes'
