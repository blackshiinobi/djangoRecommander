from django.shortcuts import render
from showMovies.models import movie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
	film = movie.objects.all()
	paginator = Paginator(film, 20)

	page = request.GET.get('page')

	m = paginator.get_page(page)

	api_key = "a8a96c562bbd8c7f6f192b5cefcf9c79"
	return render(request, 'showMovies/index.html', {'movies': m, 'api_key': api_key})

def posterTest(request):
	film = movie.objects.all()
	paginator = Paginator(film, 20)
	page = request.GET.get('page')
	m = paginator.get_page(page)

	api_key = "a8a96c562bbd8c7f6f192b5cefcf9c79"
	return render(request, 'showMovies/posterTest.html', {'movies': m, 'api_key': api_key})