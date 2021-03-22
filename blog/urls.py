from django.urls import path, re_path

from . import views


app_name = "bloga"

urlpatterns = [
    path('', views.blog_view, name='blog'),
    re_path(r'article/(?P<slug>[-\w]+)/', views.article_detail),
]
