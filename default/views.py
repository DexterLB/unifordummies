from functools import reduce

from django.shortcuts import render
from django.views.generic import ListView

from default import models


class ProgrammeListView(ListView):
    model = models.Programme
    templates = 'default/programme_list'
    context_object_name = 'programmes'


def index_page_view(request):
    spec_cat_cat = models.SpecCategoryCategory.objects.all()
    spec_cat = models.SpecCategory.objects.all().order_by('name')
    return render(request, 'default/index.html',
                  {'spec_cat_cat': spec_cat_cat,
                   'spec_cat': spec_cat})


def search_cat_view(request, id):
    results = models.Programme.objects.filter(categories__id=id)
    return render(request, 'default/search.html',
                  {'results': results})


# MAGIC: Don't touch!
# When I wrote this, only God and I understood what I was doing.
# Now, only God knows.
def search_page_view(request):
    if request.method == 'POST':
        req_dict = request.POST
        chosen_categories_ids = \
            [int(x[:-4]) for x in req_dict.keys() if 'on' in req_dict[x]]
        ch_cats = models.SpecCategory.objects.filter(
            id__in=chosen_categories_ids)
        results = list(reduce(lambda x, y: set(x) & set(y),
                       [models.Programme.objects.filter(categories=cat)
                       for cat in ch_cats]))
        return render(request, 'default/search.html',
                      {'results': results})


def programme_view(request, id):
    programme = models.Programme.objects.get(id=id)
    return render(request, 'default/progrmame.html',
                  {'programme': programme})
