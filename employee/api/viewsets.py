from rest_framework import viewsets
from employee.api import serializers
from employee import models

class EmployeeViewset(viewsets.ModelViewSet):

    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()
