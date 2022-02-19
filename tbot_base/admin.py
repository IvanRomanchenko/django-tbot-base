from django.contrib import admin

from .models import BotConfig


@admin.register(BotConfig)
class BotConfigAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'token', 'server_url', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)

    def has_delete_permission(self, request, obj=None):
        return False
