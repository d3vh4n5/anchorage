from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import *

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
    return render(request, 'anchorage/index.html', context)

def login(request):
    return render(request, 'anchorage/pages/login.html')


def userpage(request):
    context = {
        "lista" : [
            "enlace1",
            "enlace2",
            "enlace3",
            "enlace4",
            "enlace5",
        ],
    }
    return render(request, 'anchorage/pages/userpage.html', context)

def signup(request):
    if request.method == "POST":
        signup_form = SignUp(request.POST)
    else:
        signup_form = SignUp()
    context = {'signup_form': signup_form}
    return render(request, 'anchorage/pages/signup.html', context)


def parametro(request, data):
    return HttpResponse(data)