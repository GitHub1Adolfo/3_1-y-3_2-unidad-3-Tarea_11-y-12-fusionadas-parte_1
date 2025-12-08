from django.shortcuts import render
from tiendaApp.models import Empleado
from django.http import JsonResponse

def empleadosApi(request):
    """
    API simple que retorna todos los empleados en formato JSON
    Compatible con la implementación de la tarea 11
    """
    empleados = Empleado.objects.all()
    
    # Construir lista de empleados con todos los campos disponibles
    empleados_data = []
    for emp in empleados:
        empleado_dict = {
            'id': emp.id,
            'nombre': emp.nombre,
            'email': emp.email,
        }
        
        # Agregar campos opcionales si existen
        if emp.run:
            empleado_dict['run'] = emp.run
        if emp.paterno:
            empleado_dict['paterno'] = emp.paterno
        if emp.apellido:
            empleado_dict['apellido'] = emp.apellido
        if emp.telefono:
            empleado_dict['telefono'] = emp.telefono
        # Usando sueldo o salario
        if emp.sueldo:
            empleado_dict['sueldo'] = float(emp.sueldo)
        if emp.salario:
            empleado_dict['salario'] = float(emp.salario)
        if emp.cargo:
            empleado_dict['cargo'] = emp.cargo
        if emp.departamento:
            empleado_dict['departamento'] = emp.departamento
        if emp.fecha_contratacion:
            empleado_dict['fecha_contratacion'] = emp.fecha_contratacion.strftime('%Y-%m-%d')
        if emp.fotografia:
            empleado_dict['fotografia'] = emp.fotografia.url
        
        empleados_data.append(empleado_dict)
    
    data = {
        'empleados': empleados_data,
        'total': empleados.count()
    }
    
    return JsonResponse(data, safe=False)