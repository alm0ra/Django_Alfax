from django.urls import path, re_path

from . import views


app_name="landing"
urlpatterns = [
    path('', views.index, name='land'),
    path('resume/', views.resume, name= 'resume')
]
