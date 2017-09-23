from django.http import HttpResponse, HttpResponseRedirect
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
    # if request.POST:
    #     user_name = request.POST['user_name']
    #     password = request.POST['password']
    #     repeat_password = request.POST['repeat_password']
    #     email = request.POST['email']
    # return HttpResponseRedirect('/')
    return render(request, 'signup.html')


def signup_user(request):
    if request.POST:
        user_name = request.POST['user_name']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        email = request.POST['email']
    return HttpResponseRedirect('/')


def login(request):
    return render(request, 'login.html')


def check_user_name(request):
    if request.GET:
        user_name = request.GET['user_name']
        print(user_name)
        names = {'Katya', 'Igor', 'Maxim', 'Anna'}
        result = 'no'
        if user_name in names:
            result = 'ok'

        return HttpResponse(result, content_type='text/html')
    else:
        pass

