from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.blog_view, name='blog'),
]
