from django.shortcuts import render
from django.http import JsonResponse
# Importa el modelo central para interactuar con la BD
from tiendaApp.models import Empleado 

def employeeView_2(request):
    # Ejemplo 2: Devolver datos desde la BD usando Empleado
    empleados = Empleado.objects.all()
    data = {
        'employees': list(empleados.values('nombre', 'apellido', 'email', 'salario', 'cargo'))
    }
    return JsonResponse(data, safe=False)

# Nota: La función 'employeeView' de la demo original (hardcodeada) ha sido omitida.