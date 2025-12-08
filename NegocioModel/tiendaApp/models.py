from django.db import models

class Empleado(models.Model):
    # Campos de la tarea 11
    run = models.CharField(max_length=12, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    paterno = models.CharField(max_length=100, null=True, blank=True)
    
    # Campos de la tarea 12
    apellido = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cargo = models.CharField(max_length=100, null=True, blank=True)
    departamento = models.CharField(max_length=100, null=True, blank=True)
    fotografia = models.ImageField(upload_to='empleados/', null=True, blank=True)
    fecha_contratacion = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['id']
    
    def __str__(self):
        if self.apellido:
            return f"{self.nombre} {self.apellido}"
        elif self.paterno:
            return f"{self.nombre} {self.paterno}"
        return self.nombre