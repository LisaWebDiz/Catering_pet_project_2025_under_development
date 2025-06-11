from django.contrib import admin

from app.models import Unit


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    list_display_links = ('id', 'name')
    list_filter = ('user', 'name')
    search_fields = ('name',)
    raw_id_fields = ('user',)
