from django.contrib import admin

from app.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'recipe', 'presentation', 'min_portioning')
    list_display_links = ('id', 'name')
    list_filter = ('user', 'name', 'presentation')
    search_fields = ('name',)
