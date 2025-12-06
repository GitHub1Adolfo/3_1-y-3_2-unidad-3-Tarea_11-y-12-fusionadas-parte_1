from django.shortcuts import render
from rest_framework import viewsets

from viewsetApp.models import Student
from viewsetApp.serializers import StudentSerializer

# Create your views here.
class StudentViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer