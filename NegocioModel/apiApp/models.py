from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return f"{self.id} {self.name} (${self.salary})"