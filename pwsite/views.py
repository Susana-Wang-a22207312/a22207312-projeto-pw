from django.shortcuts import render
from datetime import datetime

def index_view(request):
    return render(request, "index.html", {'data' : datetime.today()})

def sobre_view(request):
    return render(request, "sobre.html", {'data' : datetime.today()})

def interesses_view(request):
    return render(request, "interesses.html", {'data' : datetime.today()})
