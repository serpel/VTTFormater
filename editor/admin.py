# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import QuillPost

@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass

# Register your models here.
