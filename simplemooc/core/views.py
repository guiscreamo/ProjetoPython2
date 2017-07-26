from django.shortcuts import render
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'index.html')

def home(request):
	return render(request, 'home.html')

def contato(request):
	return render(request, 'contato.html')

