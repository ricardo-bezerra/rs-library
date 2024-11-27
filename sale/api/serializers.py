from rest_framework import serializers
from sale.models import Sale, PaymentMethod, Condition


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
       
        model = Sale
       
        fields = ('__all__')
