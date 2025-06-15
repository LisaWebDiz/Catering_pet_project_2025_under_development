from rest_framework import serializers

from app.models import Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'user', 'name', 'presentation', 'recipe', 'products', 'cooking_tools', 'min_portioning']

    validators = [
        serializers.UniqueTogetherValidator(
            queryset=Dish.objects.all(),
            fields=('user', 'name'),
            message='Такое блюдо уже существует'
        )
    ]