from django.db import models

# Create your models here.
class Employee(models.Model):
    
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    sueldo_base = models.FloatField()
    horas_trabajadas = models.DateTimeField(auto_now=True)
    telefono = models.CharField(max_length = 14)

    def __str__(self):
        return self.nombre