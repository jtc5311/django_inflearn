from django.shortcuts import render
from .models import Post, Category #models에 있는 post를 가져와라
from django.views.generic import ListView, DetailView #리스트뷰 기능 (장고 기능)

# Create your views here.
'''
def index(request):
    posts = Post.objects.all() # index.html for문에 들어감 post 모든걸 가져와서 posts라는 변수에 저장 (장고 기본 제공)
    #모델을 불러와서
    return render(
        request,
        'blog/index.html', #템플릿에 넣고
        {
            'posts': posts, #딕셔너리에 담음 
            'a_plus_b': 1 + 3,
        }
    )
'''

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count() # 특정 조건만 가져옴

        return context
        


class PostDetail(DetailView):
    model = Post

'''
def post_detail(request, pk):
    blog_post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {
            'blog_post': blog_post,
        }
    )
'''