# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Genre

# Create your views here.
def index(request):
	list_of_albums = Album.objects.order_by('name')
	output = ', '.join([album.name for album in list_of_albums])
	return HttpResponse(output)

def album(request, album_id):
	return HttpResponse("Youre looking at album %s" % album_id)

def genre(request, genre_id):
	return HttpResponse("You're looking at genre %s" % genre_id)

	

