from django.http import JsonResponse
from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

# from app.filters import UnitFilter
# from app.forms.category import UnitForm
# from app.mixins.view_mixins import UserQuerySetMixin
from app.models import Unit
from app.pagination import CustomPagination
from app.serializers.unit import UnitSerializer


@extend_schema(tags=['Единицы измерения'])
@extend_schema_view(
    list=extend_schema(summary='Единицы измерения: просмотр списка всех записей', ),
    update=extend_schema(summary='Единица измерения: изменение конкретной записи', ),
    partial_update=extend_schema(summary='Единица измерения: частичное изменение конкретной записи', ),
    create=extend_schema(summary='Единица измерения: создание новой записи', ),
    retrieve=extend_schema(summary='Единица измерения: просмотр конкретной записи', ),
    destroy=extend_schema(summary='Единица измерения: удаление конкретной записи', ),
)
class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filterset_class = UnitFilter
    ordering_fields = ['name', ]
    search_fields = ['name', ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)