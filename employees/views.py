from django.shortcuts import render

# Create your views here.
from .models import Employee
from rest_framework import viewsets
from .serializers import EmployeeSerializer
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    

