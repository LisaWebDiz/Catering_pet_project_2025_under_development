from django.contrib import admin

from app.models import DishProduct


@admin.register(DishProduct)
class DishProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'dish', 'product', 'unit', 'amount')
    list_display_links = ('id',)
    list_filter = ('user', )
    search_fields = ('dish__name',)
    raw_id_fields = ('user', 'dish', 'product', 'unit')
