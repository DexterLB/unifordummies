from django.shortcuts import *
from default import models

def post(request):
    return render(request, 'unifordummies/post.html', {'post': int(request.GET['pid'])})

def posts(request):
    if request.method == 'GET':
        programme_ = request.GET['programme']
    elif request.method == 'POST':
        programme_ = request.POST['programme']

    try:
        page = int(request.GET['page'])
        posts = Posts.objects.get(programme = programme_)
    except DoesNotExist:
        return render(request, 'unifordummies/error.html', {'error': 'Page does not exist'})

    if page * i < len(posts):
        return render(request, 'unifordummies/posts.html', {'posts': posts[page - 1 * i : 20]})
    else:
        return render(request, 'unifordummies/error.html', {'error': 'Page does not exist'})

def index(request):
    return render_to_response('unifordummies/index.html')
