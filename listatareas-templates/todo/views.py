from django.shortcuts import render, redirect
from .forms import AgregarTareas

tareas = ["aprende django", "estudiar algo", "aprender python"]

def home(request):
    #la variable context creo que se puede poner por lo que quieras
    context = {"tareas" : tareas}
    return render(request, "todo/home.html", context)

def addlist(request):
    if request.method == "POST":
        #MIRAR LO QUE HAY EN LA CAJA DEL FORMULARIO
        formulario = AgregarTareas(request.POST)
        if formulario.is_valid():
            tarea = formulario.cleaned_data["tarea"]
            tareas.append(tarea)
            return redirect("home")
    else:
        formulario = AgregarTareas()


    context = {"formulario" : formulario}
    return render(request, "todo/add.html", context)