from django.db import models

# Create your models here.
class  Proyecto(models.Model):
    nombre = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre
    




class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    horas = models.IntegerField()
    descripcion = models.TextField()
    estado = models.BooleanField()
    codigo = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    fecha = models.DateTimeField()


    def __str__(self):
        return self.nombre 
