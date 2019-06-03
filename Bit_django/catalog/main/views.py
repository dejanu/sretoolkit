# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from main.models import Student

# Create your views here.
def index(request):
    return HttpResponse('<p>Index view</p>')

def entry_detail(request,nume):
    return HttpResponse('<p>entry_detail cu numele  '+str(nume)+' </p>')
