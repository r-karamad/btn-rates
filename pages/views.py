from urllib import request
from django.shortcuts import render
import json

from . import tasks

def HomePageView(request):
    template_name = "home.html"
    return render(request, 'home.html', tasks.get_exchange_rates())
