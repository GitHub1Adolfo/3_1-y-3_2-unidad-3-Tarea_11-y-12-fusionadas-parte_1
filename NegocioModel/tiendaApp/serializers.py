from rest_framework import serializers
from tiendaApp.models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    """
    Serializer que muestra todos los campos de Empleado y maneja validaciones.
    """
    
    class Meta:
        model = Empleado
        fields = '__all__'
        read_only_fields = ('id',)
        exclude = []
    
    def validate_salario(self, value):
        """Valida que el salario sea mayor a 0"""
        if value is not None and value <= 0:
            raise serializers.ValidationError("El salario debe ser mayor a 0")
        return value
    
    def validate_sueldo(self, value):
        """Valida que el sueldo sea mayor a 0"""
        if value is not None and value <= 0:
            raise serializers.ValidationError("El sueldo debe ser mayor a 0")
        return value
    
    def validate_email(self, value):
        """Valida que el email sea único al actualizar"""
        if self.instance:
            if Empleado.objects.exclude(pk=self.instance.pk).filter(email=value).exists():
                raise serializers.ValidationError("Este email ya está registrado")
        else:
            if Empleado.objects.filter(email=value).exists():
                raise serializers.ValidationError("Este email ya está registrado")
        return value
    
    def validate_run(self, value):
        """Valida que el RUN sea único si se proporciona"""
        if value:
            if self.instance:
                if Empleado.objects.exclude(pk=self.instance.pk).filter(run=value).exists():
                    raise serializers.ValidationError("Este RUN ya está registrado")
            else:
                if Empleado.objects.filter(run=value).exists():
                    raise serializers.ValidationError("Este RUN ya está registrado")
        return value