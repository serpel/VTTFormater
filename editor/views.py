# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render
from .models import QuillPost
from django.views.generic import UpdateView
from .compact import get_vtt
import json

# Create your views here.
from .forms import QuillFieldForm

class QuillPostUpdateView(UpdateView):
    model = QuillPost
    fields = ['output']

def editor_view(request):
    form = QuillFieldForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dataJson = vtt_formater(form.cleaned_data['content'])
            form = QuillFieldForm()
            return render(request, 'result.html', {'form': form, 'data' : dataJson})

    return render(request, 'editor.html', {'form': form})

def vtt_formater(input):
    parsed_json = (json.loads(input))
    parsed_json = (json.loads(parsed_json["delta"]))
    parsed_json = parsed_json['ops'][0]['insert']
    return get_vtt(parsed_json)