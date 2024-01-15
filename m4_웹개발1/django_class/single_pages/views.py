from django.shortcuts import render
from blog.models import Post

def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts':recent_posts,
        }
    )

def about_me(request):
    return render(request, "single_pages/about_me.html")

# 장고에서 templates 폴더는 html파일이 있는 곳으로 인식함.