# import requests
from django.shortcuts import render, get_object_or_404
from .models import *

def movie_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    movies = Movie.objects.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        movies = movies.filter(category=current_category)
    return render(request,
                  'taste/list.html',
                  {
                      'current_category':current_category,
                      'categories':categories,
                      'movies':movies
                  })

def movie_detail(request, id, movie_slug=None):
    movie = get_object_or_404(Movie, id=id, slug=movie_slug)
    return render(request, 'taste/detail.html', {'movie':movie})

def about_me(request):
    return render(request, 'taste/about-me.html')

def contact(request):
    return render(request, 'taste/contact.html')

def movieplay(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    movies = Movie.objects.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        movies = movies.filter(category=current_category)
    return render(request,
                  'taste/movies.html',
                  {
                      'current_category':current_category,
                      'categories':categories,
                      'movies':movies
                  })
