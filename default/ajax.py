import json

from django.http import HttpResponse, Http404

from default.models import Post


def vote(request, post_id, direction):
    if request.is_ajax():
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            data = {'success': False}
            data = json.dumps(data)
            return HttpResponse(data,
                                content_type='application/json')

        if direction == 'up':
            post.vote += 1
        elif direction == 'down':
            post.vote -= 1
        else:
            raise Http404
        post.save()

        data = {
            'success': True,
            'votes': post.vote,
        }
        data = json.dumps(data)
        return HttpResponse(data,
                            content_type='application/json')
    else:
        raise Http404
