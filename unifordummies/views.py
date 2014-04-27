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
        request.session['results'] = results
        return render(request, 'unifordummies/search.html', {'results': request.session['results']})


def programme_view(request, id):
    programme = models.Programme.objects.get(id = id)
    return render(request, 'unifordummies/programme.html', {'programme': programme, {'others': request.session['results'][:10]}})


def post_view(request, postid):
    post = models.Post.objects.get(id = postid)
    return render(request, 'unifordummies/post.html', {'programme': post.programme, 'post': post, {'others': request.session['results'][:10]}})


def posts_view(request, prid, pid):
    posts = models.Posts.objects.filter(programme = prid).order_by('vote')
    paginator = Paginator(posts, 20)
    try:
        posts = paginator.page(pid)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'unifordummies/posts.html', {'programme': models.Programme.objects.get(id = prid), 'posts': posts, {'others': request.session['results'][:10]}})


def index(request):
    return render_to_response('unifordummies/index.html')
