"""
===========================================================
genericsApp/serializers.py
===========================================================
"""
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Employee (genericsApp)
    Usado con Generic Views
    """
    
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('id',)
    
    def validate_salary(self, value):
        """Valida que el salario sea mayor a 0"""
        if value <= 0:
            raise serializers.ValidationError(
                "El salario debe ser mayor a 0"
            )
        return value
    
    def validate_name(self, value):
        """Valida que el nombre no esté vacío"""
        if not value or value.strip() == '':
            raise serializers.ValidationError(
                "El nombre no puede estar vacío"
            )
        return value.strip()
    
    def validate_position(self, value):
        """Valida que el cargo no esté vacío"""
        if not value or value.strip() == '':
            raise serializers.ValidationError(
                "El cargo no puede estar vacío"
            )
        return value.strip()