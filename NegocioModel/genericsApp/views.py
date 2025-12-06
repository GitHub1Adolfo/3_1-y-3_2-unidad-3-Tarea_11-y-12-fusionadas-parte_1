from django.shortcuts import render
from rest_framework import generics

from genericsApp.models import Student
from genericsApp.serializers import StudentSerializer

# Create your views here.
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer