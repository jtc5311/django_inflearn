from django.shortcuts import render
from .models import Post #models에 있는 post를 가져와라

# Create your views here.

def index(request):
    posts = Post.objects.all() # index.html for문에 들어감 post 모든걸 가져와서 posts라는 변수에 저장 (장고 기본 제공)
    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
            'a_plus_b': 1 + 3,
        }
    )