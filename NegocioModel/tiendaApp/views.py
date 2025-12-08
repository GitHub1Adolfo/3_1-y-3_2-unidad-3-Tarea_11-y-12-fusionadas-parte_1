from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tiendaApp.models import Empleado
from tiendaApp.serializers import EmpleadoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# ============================================
# VISTAS WEB TRADICIONALES (tarea 11)
# ============================================

def inicio(request):
    """Vista principal que muestra el listado de empleados"""
    empleados = Empleado.objects.all()
    return render(request, 'tiendaApp/inicio.html', {
        'empleados': empleados
    })

@login_required
def crear_empleado(request):
    """Crea un nuevo empleado"""
    if request.method == 'POST':
        try:
            empleado = Empleado(
                run=request.POST.get('run'),
                nombre=request.POST.get('nombre'),
                paterno=request.POST.get('paterno'),
                apellido=request.POST.get('apellido'),
                email=request.POST.get('email'),
                telefono=request.POST.get('telefono'),
                sueldo=request.POST.get('sueldo'),
                salario=request.POST.get('salario'),
                cargo=request.POST.get('cargo'),
                departamento=request.POST.get('departamento'),
                fecha_contratacion=request.POST.get('fecha_contratacion')
            )
            
            if 'fotografia' in request.FILES:
                empleado.fotografia = request.FILES['fotografia']
            
            empleado.save()
            messages.success(request, 'Empleado creado exitosamente')
            return redirect('inicio')
        except Exception as e:
            messages.error(request, f'Error al crear empleado: {str(e)}')
    
    return render(request, 'tiendaApp/empleado_form.html')

@login_required
def cargar_editar_empleado(request, empleado_id):
    """Carga el formulario para editar un empleado"""
    empleado = get_object_or_404(Empleado, id=empleado_id)
    return render(request, 'tiendaApp/empleado_form.html', {
        'empleado': empleado,
        'editar': True
    })

@login_required
def editar_empleado(request, empleado_id):
    """Actualiza los datos de un empleado"""
    empleado = get_object_or_404(Empleado, id=empleado_id)
    
    if request.method == 'POST':
        try:
            empleado.run = request.POST.get('run', empleado.run)
            empleado.nombre = request.POST.get('nombre', empleado.nombre)
            empleado.paterno = request.POST.get('paterno', empleado.paterno)
            empleado.apellido = request.POST.get('apellido', empleado.apellido)
            empleado.email = request.POST.get('email', empleado.email)
            empleado.telefono = request.POST.get('telefono', empleado.telefono)
            empleado.sueldo = request.POST.get('sueldo', empleado.sueldo)
            empleado.salario = request.POST.get('salario', empleado.salario)
            empleado.cargo = request.POST.get('cargo', empleado.cargo)
            empleado.departamento = request.POST.get('departamento', empleado.departamento)
            empleado.fecha_contratacion = request.POST.get('fecha_contratacion', empleado.fecha_contratacion)
            
            if 'fotografia' in request.FILES:
                empleado.fotografia = request.FILES['fotografia']
            
            empleado.save()
            messages.success(request, 'Empleado actualizado exitosamente')
            return redirect('inicio')
        except Exception as e:
            messages.error(request, f'Error al actualizar empleado: {str(e)}')
    
    return redirect('editarEmpleado', empleado_id=empleado_id)

@login_required
def eliminar_empleado(request, empleado_id):
    """Elimina un empleado"""
    empleado = get_object_or_404(Empleado, id=empleado_id)
    try:
        empleado.delete()
        messages.success(request, 'Empleado eliminado exitosamente')
    except Exception as e:
        messages.error(request, f'Error al eliminar empleado: {str(e)}')
    
    return redirect('inicio')

# ============================================
# API RESTful con Django REST Framework (tarea 12)
# ============================================

@api_view(['GET', 'POST'])
def empleado_listado(request):
    """
    GET: Lista todos los empleados
    POST: Crea un nuevo empleado
    """
    if request.method == 'GET':
        empleados = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleados, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def empleado_detalle(request, pk):
    """
    GET: Obtiene un empleado específico
    PUT: Actualiza un empleado
    DELETE: Elimina un empleado
    """
    try:
        empleado = Empleado.objects.get(id=pk)
    except Empleado.DoesNotExist:
        return Response(
            {'error': 'Empleado no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = EmpleadoSerializer(empleado, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        empleado.delete()
        return Response(
            {'message': 'Empleado eliminado exitosamente'},
            status=status.HTTP_204_NO_CONTENT
        )