from django.http import HttpResponse
from django.shortcuts import render
from rss.apps.rss_news.models import Post

# Create your views here.


def index(request):
    posts = reversed(Post.objects.all())
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def post(request, index):
    try:
        post = Post.objects.get(id=index)
        result = post.text
    except Post.DoesNotExist:
        result = 'Post does not exist!'
    return HttpResponse(result)


def log_form(request):
    return render(request, 'log_form.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')
