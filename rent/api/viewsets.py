from rest_framework import viewsets
from rent.api import serializers
from rent import models

class RentViewset(viewsets.ModelViewSet):

    serializer_class = serializers.RentSerializer
    queryset = models.Rent.objects.all()
