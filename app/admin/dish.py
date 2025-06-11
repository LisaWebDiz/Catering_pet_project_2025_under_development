from django.contrib import admin

from app.models import Dish, DishProduct

class DishProductInline(admin.TabularInline):
    model = DishProduct
    fields = ('dish',)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'recipe', 'presentation', 'min_portioning')
    list_display_links = ('id', 'name')
    list_filter = ('user', 'presentation')
    search_fields = ('name',)
    inlines = [DishProductInline]
    raw_id_fields = ('user', )
    autocomplete_fields = ('cooking_tools',)

