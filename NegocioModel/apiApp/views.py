from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

# Create your views here.
def employeeView(request):
    # Ejemplo 1: Devolver un diccionario hardcoded
    emp = {
        'id': 123,
        'name': 'Clark',
        'email': 'sup@jl.org',
        'salary': '5000'
    }
    return JsonResponse(emp)

def employeeView_2(request):
    # Ejemplo 2: Devolver datos desde la BD
    empleados = Employee.objects.all()  # Obtiene todos los empleados
    data = {
        'employees': list(empleados.values('name', 'salary'))
    }
    return JsonResponse(data)