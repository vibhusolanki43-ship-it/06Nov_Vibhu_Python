from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer