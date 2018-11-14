from django.shortcuts import render

def index(request):
    number = 6
    thing = "your family"
    return render(request, 'index.html', {
        'number': number,
        'thing': thing,
    })
