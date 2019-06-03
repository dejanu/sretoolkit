# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    nume=models.CharField(max_length=30)
    prenume=models.CharField(max_length=30)
    description=models.TextField()
    proiect=models.FileField(upload_to='proiecte/')
    email=models.EmailField(unique=True)
    nota=models.IntegerField(default=0)
