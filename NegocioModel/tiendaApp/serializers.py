from rest_framework import serializers
from serialApp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # Todos los campos del modelo