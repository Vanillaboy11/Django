from django.shortcuts import render
from django.http import HttpResponse #pagina_web/views.py

# Create your views here.

def vistaPaginaDeInicio(solicitud):
    return HttpResponse('Hola mundo!')