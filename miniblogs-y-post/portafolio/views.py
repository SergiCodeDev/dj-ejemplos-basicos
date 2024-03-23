from django.shortcuts import render
from .models import Projecto

# Create your views here.

def inicio(request):
    # esto importa los projectos de la base de datos
    projects = Projecto.objects.all()

    return render(request, "portafolio/inicio.html", { "projects":  projects})