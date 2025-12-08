from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Importa el modelo y serializer del core
from tiendaApp.models import Empleado
from tiendaApp.serializers import EmpleadoSerializer

@api_view(['GET', 'POST'])
def employee_list(request):
    """List all employees (Empleados) or create a new one."""
    if request.method == 'GET':
        empleados = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleados, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    """Retrieve, update or delete an employee (Empleado) instance."""
    try:
        empleado = Empleado.objects.get(pk=pk)
    except Empleado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = EmpleadoSerializer(empleado, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        empleado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)