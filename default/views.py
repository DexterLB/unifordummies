from functools import reduce

from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage
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
    results_sorted = _sort_results(results)
    return render(request, 'default/search.html',
                  {'results': results_sorted})


# MAGIC: Don't touch!
# When I wrote this, only God and I understood what I was doing.
# Now, only God knows.
# All hail to the God of Functional Programming!
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
        results_sorted = _sort_results(results)
        return render(request, 'default/search.html',
                      {'results': results_sorted})


def _sort_results(results):
    results_sorted = sorted(results, key=lambda x: x.rating, reverse=True)
    return results_sorted


def programme_view(request, programme_id):
    programme = models.Programme.objects.get(id=programme_id)
    most_voted_posts = [post for post in
                        programme.posts.all().order_by('-vote')[:3]]
    return render(request, 'default/programme.html', {
        'programme': programme,
        'most_voted_posts': most_voted_posts,
    })


def posts_view(request, programme_id, cat_id, page_id):
    programme = models.Programme.objects.get(id=programme_id)
    if cat_id:
        posts = models.Post.objects\
            .filter(category__id=cat_id, programme__id=programme_id)\
            .order_by('-vote')
    else:
        posts = models.Post.objects\
            .filter(programme__id=programme_id)\
            .order_by('-vote')
    paginator = Paginator(posts, 20)
    try:
        posts_page = paginator.page(page_id)
    except EmptyPage:
        posts_page = paginator.page(paginator.num_pages)
    return render(request, 'default/posts.html', {
        'programme': programme,
        'posts': posts_page
    })
