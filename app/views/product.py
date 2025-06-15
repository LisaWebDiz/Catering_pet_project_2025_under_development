from django.http import JsonResponse
from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

# from app.filters import ProductFilter
# from app.forms.category import ProductForm
# from app.mixins.view_mixins import UserQuerySetMixin
from app.models import Product
from app.pagination import CustomPagination
from app.serializers.product import ProductSerializer


@extend_schema(tags=['Продукты'])
@extend_schema_view(
    list=extend_schema(summary='Продукты: просмотр списка всех записей', ),
    update=extend_schema(summary='Продукт: изменение конкретной записи', ),
    partial_update=extend_schema(summary='Продукт: частичное изменение конкретной записи', ),
    create=extend_schema(summary='Продукт: создание новой записи', ),
    retrieve=extend_schema(summary='Продукт: просмотр конкретной записи', ),
    destroy=extend_schema(summary='Продукт: удаление конкретной записи', ),
)
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filterset_class = ProductFilter
    ordering_fields = ['name', ]
    search_fields = ['name', ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)