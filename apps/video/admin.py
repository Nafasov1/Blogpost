from django.contrib import admin

from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')
    list_display_links = ('id', 'title')
    list_filter = ('created_date',)
    search_fields = ('id', 'title')
    date_hierarchy = 'created_date'
