"""
===========================================================
viewsetApp/serializers.py
===========================================================
"""
from rest_framework import serializers
from .models import Employee
from datetime import date

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Employee (viewsetApp)
    Usado con ViewSets y Router
    """
    
    # Campos calculados adicionales
    years_of_service = serializers.SerializerMethodField()
    salary_category = serializers.SerializerMethodField()
    full_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('id',)
        # Si quieres incluir los campos calculados:
        # fields = ['id', 'name', 'position', 'salary', 'hire_date', 
        #           'years_of_service', 'salary_category', 'full_info']
    
    def get_years_of_service(self, obj):
        """Campo calculado: años de servicio"""
        if obj.hire_date:
            today = date.today()
            years = today.year - obj.hire_date.year
            # Ajustar si aún no ha cumplido años este año
            if (today.month, today.day) < (obj.hire_date.month, obj.hire_date.day):
                years -= 1
            return years
        return 0
    
    def get_salary_category(self, obj):
        """Campo calculado: categoría según salario"""
        if obj.salary >= 3000000:
            return 'Alto'
        elif obj.salary >= 1500000:
            return 'Medio'
        elif obj.salary >= 500000:
            return 'Bajo'
        else:
            return 'Inicial'
    
    def get_full_info(self, obj):
        """Campo calculado: información completa del empleado"""
        return f"{obj.name} - {obj.position} (${obj.salary:,.0f})"
    
    def validate_salary(self, value):
        """Valida que el salario sea mayor a 0"""
        if value <= 0:
            raise serializers.ValidationError(
                "El salario debe ser mayor a 0"
            )
        # Validación adicional: salario máximo
        if value > 50000000:
            raise serializers.ValidationError(
                "El salario no puede exceder $50,000,000"
            )
        return value
    
    def validate_name(self, value):
        """Valida que el nombre no esté vacío y tenga longitud adecuada"""
        if not value or value.strip() == '':
            raise serializers.ValidationError(
                "El nombre no puede estar vacío"
            )
        if len(value.strip()) < 2:
            raise serializers.ValidationError(
                "El nombre debe tener al menos 2 caracteres"
            )
        return value.strip()
    
    def validate_position(self, value):
        """Valida que el cargo no esté vacío"""
        if not value or value.strip() == '':
            raise serializers.ValidationError(
                "El cargo no puede estar vacío"
            )
        return value.strip()
    
    def validate_hire_date(self, value):
        """Valida que la fecha de contratación no sea futura"""
        if value > date.today():
            raise serializers.ValidationError(
                "La fecha de contratación no puede ser futura"
            )
        return value
    
    def validate(self, data):
        """
        Validación a nivel de objeto
        Se ejecuta después de todas las validaciones de campo
        """
        # Ejemplo: gerentes deben tener salario mínimo
        position = data.get('position', '').lower()
        salary = data.get('salary', 0)
        
        if 'gerente' in position and salary < 2000000:
            raise serializers.ValidationError({
                'salary': 'Los gerentes deben tener un salario mínimo de $2,000,000'
            })
        
        # Ejemplo: directores deben tener salario mínimo mayor
        if 'director' in position and salary < 3000000:
            raise serializers.ValidationError({
                'salary': 'Los directores deben tener un salario mínimo de $3,000,000'
            })
        
        return data
    
    def create(self, validated_data):
        """
        Personalizar la creación de instancias
        Se ejecuta cuando se llama serializer.save() en POST
        """
        # Aquí puedes agregar lógica adicional antes de crear
        employee = Employee.objects.create(**validated_data)
        
        # Ejemplo: logging, enviar email de bienvenida, etc.
        print(f"Nuevo empleado creado: {employee.name} - {employee.position}")
        
        return employee
    
    def update(self, instance, validated_data):
        """
        Personalizar la actualización de instancias
        Se ejecuta cuando se llama serializer.save() en PUT/PATCH
        """
        # Guardar valores anteriores para comparación
        old_salary = instance.salary
        old_position = instance.position
        
        # Actualizar campos
        instance.name = validated_data.get('name', instance.name)
        instance.position = validated_data.get('position', instance.position)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.hire_date = validated_data.get('hire_date', instance.hire_date)
        instance.save()
        
        # Ejemplo: registrar cambios importantes
        if old_salary != instance.salary:
            print(f"Cambio de salario para {instance.name}: ${old_salary} -> ${instance.salary}")
        
        if old_position != instance.position:
            print(f"Cambio de cargo para {instance.name}: {old_position} -> {instance.position}")
        
        return instance