# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display=["nume","email","proiect","nota"]
    
admin.site.register(Student,studentAdmin)
