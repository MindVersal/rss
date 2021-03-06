"""rss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rss.apps.rss_news import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<index>[0-9]+)/$', views.post),
    url(r'^log_form', views.log_form),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login$', views.login, name='login'),
    url(r'^signup_user$', views.signup_user, name='signup_user'),
    url(r'check_user_name/$', views.check_user_name, name='check_user_name'),
]
