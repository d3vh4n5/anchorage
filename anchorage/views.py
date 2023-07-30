from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import *
from django.contrib import messages

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
    if request.method == 'POST':
        login_form = Login(request.POST)
        if login_form.is_valid():
            # redirigir al user page
            print('Login correcto')
        else:
            print("Error de autenticación")
            messages.error(request, "Usuario o contraseña incorrectos")
    else:
        login_form = Login()
    context = {'login_form' : login_form}
    return render(request, 'anchorage/pages/login.html', context)


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
        if signup_form.is_valid():
            messages.success(request, "Formulario cargado con éxito")
            print("Todo joya")
        else:
            messages.error(request, "La contraseña debe tener entre 8 y 10 caracteres")
            print("Todo mal")
    else:
        signup_form = SignUp()
    context = {'signup_form': signup_form}
    return render(request, 'anchorage/pages/signup.html', context)


def parametro(request, data):
    return HttpResponse(data)