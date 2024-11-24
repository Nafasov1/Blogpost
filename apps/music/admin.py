from django.contrib import admin

from .models import Music


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'created_date')
    list_display_links = ('id', 'owner', 'title')
    list_filter = ('owner', 'created_date')
    search_fields = ('id', 'title')
    date_hierarchy = 'created_date'
