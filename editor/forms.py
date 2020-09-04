# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django_quill.forms import QuillFormField
from .models import QuillPost

class QuillFieldForm(forms.Form): 
    content = QuillFormField()
