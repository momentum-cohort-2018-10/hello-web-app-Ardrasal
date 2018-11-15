from django.shortcuts import render
from collection.models import Place

def index(request):
    places = Place.objects.all()
    return render(request, 'index.html', {
        'places': places,
    })

def place_detail(request, slug):
    place = Place.objects.get(slug=slug)
    return render(request, 'places/place_detail.html', {
        'place': place,

    })
