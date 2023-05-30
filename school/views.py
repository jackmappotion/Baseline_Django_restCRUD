from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Students
from .serializers import StudentsSerializer

class StudentsListAPI(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentsDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer