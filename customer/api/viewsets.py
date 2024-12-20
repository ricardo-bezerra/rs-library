from rest_framework import viewsets
from customer.api import serializers
from customer import models

class CustomerViewset(viewsets.ModelViewSet):

    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.all()
