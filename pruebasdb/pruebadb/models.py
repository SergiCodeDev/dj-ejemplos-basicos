from django.db import models

class Empresa(models.Model):
    #valores para base de datos
    nombre = models.CharField(max_length=30)
    fundacion = models.IntegerField()
    #lo que se ve en el admin de django
    def __str__(self) :
        return self.nombre

#no poner en prural en dj en admin le añade una s al final
class Lenguaje(models.Model):
    nombre = models.CharField(max_length=40)
    creador = models.CharField(max_length=40, null=True)

    def __str__(self) :
        return self.nombre

class Programador(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(null=True)
    #CASCADE borra si ForeignKey esta vinculada a otra tabla superior
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,
                                related_name="empleados")
    # se vincula a tabla lenguaje puedes añadir en admin todos los lenguajes que quieras 
    lenguaje = models.ManyToManyField(Lenguaje)

    def __str__(self) :
        return self.nombre