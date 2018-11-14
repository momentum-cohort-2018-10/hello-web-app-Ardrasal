from django.shortcuts import render

def index(request):
    number = 6
    place = "downtown"
    return render(request, 'index.html', {
        'number': number,
        'place': place,
    })
