from django.shortcuts import *
from default import models
from django.core.paginator import Paginator

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
            return render(request, 'unifordummies/posts.html', {'programme': programme_, 'page': page, 'posts': posts[page - 1 * i : 20]})
        else:
            return render(request, 'unifordummies/error.html', {'error': 'Page does not exist'})
    except:
        return render(request, 'unifordummies/error.html', {'error': 'Page does not exist'})

def index(request):
    return render_to_response('unifordummies/index.html')
