from django.shortcuts import render
import random

def inicio(request):
    return render(request, 'generador/inicio.html')

def contrasena(request):

    letras = list("qwertyuiopasdfghjklñzxcvbnm")
    numeros = list("1234567890")
    MAYUSCULAS = list("QWERTYUIOPASDFGHJKLÑZXCVBNM")
    caracteres = list("!@#$%^&*()")

    contra = ""

    largocontra = int(request.GET.get("length"))

    print(largocontra)

    if request.GET.get("uppercase"):
        letras.extend(MAYUSCULAS)
    if request.GET.get("special"):
        letras.extend(caracteres)
    if request.GET.get("numbers"):
        letras.extend(numeros)

    print(len(letras))
    

    desordenar = list(letras)
    random.shuffle(desordenar)
    letras = "".join(desordenar)

    

    for x in range(largocontra):
        contra += random.choice(letras)

    print(len(contra))

    valor_final = {"contra": contra}

    return render(request, 'generador/contra.html', valor_final)