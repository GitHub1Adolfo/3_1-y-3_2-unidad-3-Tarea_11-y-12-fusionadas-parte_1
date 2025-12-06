from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        db_table = 'serial_student'  # Nombre personalizado de tabla