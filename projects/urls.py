from django.urls import path, re_path
from . import views


app_name = "project"

urlpatterns = [
    re_path(r'detail/(?P<slug>[-\w]+)/', views.project_detail, name="detail"),
]
