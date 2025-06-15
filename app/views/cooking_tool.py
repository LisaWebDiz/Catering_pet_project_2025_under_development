from django.http import JsonResponse
from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

# from app.filters import CookingToolFilter
# from app.forms.category import CookingToolForm
# from app.mixins.view_mixins import UserQuerySetMixin
from app.models import CookingTool
from app.pagination import CustomPagination
from app.serializers.cooking_tool import CookingToolSerializer


@extend_schema(tags=['Кухонные инструменты'])
@extend_schema_view(
    list=extend_schema(summary='Кухонные инструменты: просмотр списка всех записей', ),
    update=extend_schema(summary='Кухонный инструмент: изменение конкретной записи', ),
    partial_update=extend_schema(summary='Кухонный инструмент: частичное изменение конкретной записи', ),
    create=extend_schema(summary='Кухонный инструмент: создание новой записи', ),
    retrieve=extend_schema(summary='Кухонный инструмент: просмотр конкретной записи', ),
    destroy=extend_schema(summary='Кухонный инструмент: удаление конкретной записи', ),
)
class CookingToolViewSet(ModelViewSet):
    queryset = CookingTool.objects.all()
    serializer_class = CookingToolSerializer
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filterset_class = CookingToolFilter
    ordering_fields = ['name', ]
    search_fields = ['name', ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)