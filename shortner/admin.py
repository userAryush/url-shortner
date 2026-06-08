from django.contrib import admin
from .models import ShortURL

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ['short_key', 'user', 'original_url', 'click_count', 'created_at', 'expires_at']
    search_fields = ['short_key', 'original_url', 'user__email']
    list_filter = ['created_at', 'expires_at']
    readonly_fields = ['click_count', 'created_at']