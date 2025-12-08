from rest_framework import viewsets
# Importa el modelo y serializer del core
from tiendaApp.models import Empleado as Employee
from tiendaApp.serializers import EmpleadoSerializer as EmployeeSerializer

class EmpleadoViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer