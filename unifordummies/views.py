from functools import reduce
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from default import models


class ProgrammeListView(ListView):
    model = models.Programme
    templates = 'unifordummies/programme_list'
    context_object_name = 'programmes'


def index_page_view(request):
    spec_cat_cat = models.SpecCategoryCategory.objects.all()
    spec_cat = models.SpecCategory.objects.all().order_by('name')
    return render(request, 'unifordummies/index.html', {'spec_cat_cat': spec_cat_cat, 'spec_cat': spec_cat})


def search_cat_view(request, id):
    results = models.Programme.objects.filter(categories__id = id)
    return render(request, 'unifordummies/search.html', {'results': results})


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
        return render(request, 'unifordummies/search.html',
                      {'results': results})


def programme_view(request, id):
    programme = models.Programme.objects.filter(id = id).order_by('name')
    return render(request, 'unifordummies/programme.html', {'programme': programme})


def post_view(request, postid):
    post = models.Post.objects.filter(id = postid).order_by('id')
    return render(request, 'unifordummies/post.html', {'post': post})


def posts_view(request, prid, pid):
    try:
        posts = Posts.objects.get(programme = prid).order_by('id')
        page = prid
        paginator = Paginator(posts, 20)
        posts = paginator.page(page)

        if page * i < len(posts):
            return render(request, 'unifordummies/posts.html', {'programme': programme_, 'posts': posts})
        else:
            return render(request, 'unifordummies/error.html', {'error': 'Page does not exist'})
    except:
        return render(request, 'unifordummies/error.html', {'error': 'Page does not exist'})


def index(request):
    return render_to_response('unifordummies/index.html')
