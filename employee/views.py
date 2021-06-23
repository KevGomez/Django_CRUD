from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from . import models
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    # queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer 

    def get_queryset(self):
        return models.Employee.objects.all()
