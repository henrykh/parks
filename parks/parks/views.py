from django.shortcuts import render
from secrets import *


def home(request):
    context = {'mapbox_access_token': MAPBOX_ACCESS_TOKEN}
    return render(request, 'home.html', context)
