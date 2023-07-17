from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    date = datetime.now()
    context = {
        "proyecto" : "Anchorage",
        "tecnología" : "django",
        "fecha" : date,
        "lista" : [
            "Una cosa",
            43,
            True
        ]
    }
    return render(request, 'index.html', context)

def login(request):
    return HttpResponse("Aquí ira el login")

def parametro(request, data):

    return HttpResponse(data)