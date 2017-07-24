# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Genre(models.Model):
	name = models.CharField(max_length=200)

class Album(models.Model):
	name = models.CharField(max_length=200)
	genre = models.ForeignKey(Genre)



