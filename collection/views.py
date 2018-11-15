from django.shortcuts import render
from collection.models import Place

def index(request):
    places = Place.objects.all()
    return render(request, 'index.html', {
        'places': places,
    })
