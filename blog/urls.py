from django.urls import path, re_path

from . import views


app_name = "bloga"

urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('article/<slug:slug>', views.article_detail, name='detail'),
]
