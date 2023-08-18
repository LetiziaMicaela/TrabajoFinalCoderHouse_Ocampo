from django.shortcuts import render
from .models import Adoptante, Gatito, Personal
from .forms import GatitoForm, AdoptanteForm, PersonalForm, BuscarGatitoForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def base(request):
    return render(request, "aplicacion/base.html")

def adoptantes(request):
    adoptantes = Adoptante.objects.all()
    return render(request, 'aplicacion/adoptantes.html', {'adoptantes': adoptantes})

def lista_gatitos(request):
    gatitos = Gatito.objects.all()
    return render(request, 'aplicacion/lista_gatitos.html', {'gatos': gatitos})

def lista_personal(request):
    personal = Personal.objects.all()
    return render(request, 'aplicacion/lista_personal.html', {'personal': personal})


#forms

def agregar_gatito(request):
    if request.method == 'POST':
        form = GatitoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GatitoForm()

    return render(request, 'aplicacion/agregar_gatito.html', {'form': form})

def agregar_adoptante(request):
    if request.method == 'POST':
        form = AdoptanteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdoptanteForm()

    return render(request, 'aplicacion/agregar_adoptante.html', {'form': form})

def agregar_personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonalForm()

    return render(request, 'aplicacion/agregar_personal.html', {'form': form})


def buscar_gatito(request):
    form = BuscarGatitoForm(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        gatitos = Gatito.objects.filter(nombre__icontains=nombre)
    else:
        gatitos = Gatito.objects.all()

    return render(request, 'aplicacion/buscar_gatito.html', {'form': form, 'gatitos': gatitos})

#_____  Login, Logout, Registracion #

def loguin_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request,"aplicacion/base.html", {"mensaje": f"Bienvenido{usuario}"})
            else:
                return render(request, "aplicacion/login.html", {"mensaje": "datos invalidos"})
        else:
            return render(request, "aplicacion/login.html", {"mensaje": "datos invalidos"})
    
    form = AuthenticationForm()

    return render(request, "aplicacion/login.html" , {"forms": miForm})

             






