from rest_framework import serializers

from app.models import CookingTool


class CookingToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingTool
        fields = ['id', 'user', 'name', 'comment']

    validators = [
        serializers.UniqueTogetherValidator(
            queryset=CookingTool.objects.all(),
            fields=('user', 'name'),
            message='Такой кухонный инструмент уже существует'
        )
    ]