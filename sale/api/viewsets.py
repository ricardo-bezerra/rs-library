from rest_framework import viewsets
from sale.api import serializers
from sale import models

class SaleViewset(viewsets.ModelViewSet):

    serializer_class = serializers.SaleSerializer
    queryset = models.Sale.objects.all()
