from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contacts'),
    path('soon/', views.sakht, name='soon'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]
