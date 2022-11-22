from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    FechaNac=models.DateField()

    def __str__(self):
        return self.nombre+" "+self.apellido
