from rest_framework import serializers

from app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'user', 'name']

    validators = [
        serializers.UniqueTogetherValidator(
            queryset=Product.objects.all(),
            fields=('user', 'name'),
            message='Такой продукт уже существует'
        )
    ]