from django.db.models import Sum
from rest_framework import serializers

from basket.models import Basket


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ['user', 'products']
