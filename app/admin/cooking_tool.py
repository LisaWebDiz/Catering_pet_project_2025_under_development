from django.contrib import admin

from app.models import CookingTool


@admin.register(CookingTool)
class CookingToolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'comment')
    list_display_links = ('id', 'name')
    list_filter = ('user',)
    search_fields = ('name',)
    raw_id_fields = ('user',)
