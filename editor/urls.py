# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import editor_view
from . import views

urlpatterns = [
    re_path(r'^.*\.html', editor_view, name='pages'),

    path('', editor_view, name="editor"),
]
