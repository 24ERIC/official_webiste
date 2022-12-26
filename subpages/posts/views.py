from django.shortcuts import render
from .models import Post


def home (request):
    featured = Post.objects.all()[::-1][0:3]
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        'object_list': featured,
        'latest': latest,
    }
    return render(request, 'home.html',context)


def post (request,slug):
    post = Post.objects.get(slug = slug)
    latest = Post.objects.order_by('-timestamp')[:3]
    context = {
        'post': post,
        'latest': latest,
    }
    return render(request, 'post.html', context)


def events(request):
    posts = Post.objects.order_by('-timestamp')

    context = {
        'posts': posts,
    }
    return render(request, 'events.html', context)