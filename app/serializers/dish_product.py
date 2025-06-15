from rest_framework import serializers

from app.models import DishProduct


class DishProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishProduct
        fields = ['id', 'user', 'dish', 'product', 'unit', 'amount']
