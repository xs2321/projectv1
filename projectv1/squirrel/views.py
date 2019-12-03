from django.http import HttpResponse
from .models import Squirrel
from django.shortcuts import render

def all_squirrels(request):
    sightings = Squirrel.objects.all()
    context = {
        'squirrels': sightings,
    }
    return render(request, 'squirrel/map.html', context)



# Create your views here.

