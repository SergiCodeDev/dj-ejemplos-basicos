from django import forms

class AgregarTareas(forms.Form):
    tarea = forms.CharField()