from django.contrib import admin

from .models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'ad_id', 'author', 'views', 'position')
    search_fields = ('title', 'author', 'ad_id')
    list_filter = ('author', 'views')
