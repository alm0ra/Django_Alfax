from django.urls import path, re_path

from . import views


app_name ="karfarmaonline"

urlpatterns = [
    path('', views.index, name='home'),
    path('mp/', views.make_project, name='project'),
    path('in/', views.project_income, name='income'),
    path('ex/', views.project_expence, name='expence'),
]
