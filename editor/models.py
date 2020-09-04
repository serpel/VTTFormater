# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django_quill.fields import QuillField


class QuillPost(models.Model):
    content = QuillField()
    
# Create your models here.