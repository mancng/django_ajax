# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from ..notes.models import *

from django.contrib import messages

def index(request):
    return render(request, 'notes/index.html')

def add_note(request):
    if request.method == "POST":
        potential_errors = Note.objects.validate(request.POST)
        if potential_errors['status'] == "error":
            for error in potential_errors['data']:
                messages.error(request, error)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')

