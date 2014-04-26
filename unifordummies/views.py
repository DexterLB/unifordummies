from django.shortcuts import *

def test(request):
    return render(request,'unifordummies/test.html', {'categories': '<span style="color: red">Hello World!</span>'})

def index(request):
    return render_to_response('unifordummies/index.html')
