from functools import reduce
from django.shortcuts import render
from django.core.paginator import Paginator
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


def index(request):
    posts_list = Post.objects.all().order_by('-id')

    paginator = Paginator(posts_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response('home/index.html',
        { 'posts' : posts },
        context_instance=RequestContext(request))


def post(request):
    return render(request, 'unifordummies/post.html', {'post': int(request.GET['pid'])})


def posts(request):
    if request.method == 'GET':
        programme_ = request.GET['programme']
    elif request.method == 'POST':
        programme_ = request.POST['programme']

    try:
        posts = Posts.objects.get(programme = programme_).order_by('pkey')
        page = int(request.GET['p'])
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
