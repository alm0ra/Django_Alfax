# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user,forget_view,logout_view,verify_view


urlpatterns = [
    path('forget/', forget_view, name="forget"),
    path('login/', login_view, name="auth-login"),
    path('register/', register_user, name="register"),\
    path('register/verify/', verify_view, name="verify"),
    path("logout/", logout_view, name="logout")
]
