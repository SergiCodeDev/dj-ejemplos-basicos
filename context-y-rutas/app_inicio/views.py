from django.shortcuts import render
#AÑADIR PARA PRUEBA
from django.http import HttpResponse

def pruebavista(request):
    return render(request, 'app_inicio/index.html')

def dart(request):
    return HttpResponse("hola dart vader")

"""

def saludar(request, nombre):
    return HttpResponse(f"HOLA {nombre} ERES NOSEQUE")

"""

def saludar(request, nombre):
    variableParaHtml = {'nombrekey' : nombre}
    return render(request, 'app_inicio/elsaludo.html', variableParaHtml)

def moneda(request):
    num = 1
    context = {'num' : num}
    return render(request, 'app_inicio/moneda.html', context)