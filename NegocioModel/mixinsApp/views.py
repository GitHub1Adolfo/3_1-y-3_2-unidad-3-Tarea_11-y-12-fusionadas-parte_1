from django.shortcuts import render
from rest_framework import generics, mixins

from mixinsApp.models import Student
from mixinsApp.serializers import StudentSerializer

# Create your views here.
class StudentList(
    mixins.ListModelMixin,    # Provee .list()
    mixins.CreateModelMixin,  # Provee .create()
    generics.GenericAPIView   # Base para Mixins
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class StudentDetail(
    mixins.RetrieveModelMixin,  # Provee .retrieve()
    mixins.UpdateModelMixin,    # Provee .update()
    mixins.DestroyModelMixin,   # Provee .destroy()
    generics.GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)