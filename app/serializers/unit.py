from rest_framework import serializers

from app.models import Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'user', 'name']

    validators = [
        serializers.UniqueTogetherValidator(
            queryset=Unit.objects.all(),
            fields=('user', 'name'),
            message='Такая единица измерения уже существует'
        )
    ]