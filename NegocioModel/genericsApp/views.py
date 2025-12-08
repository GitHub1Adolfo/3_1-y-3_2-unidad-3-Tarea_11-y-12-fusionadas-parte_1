from rest_framework import generics
# Importa el modelo y serializer del core
from tiendaApp.models import Empleado as Employee
from tiendaApp.serializers import EmpleadoSerializer as EmployeeSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer