from django.contrib import admin

from .models import Events


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'created_date')
    list_display_links = ('id', 'title')
    list_filter = ('date', 'created_date')
    search_fields = ('id', 'title')
    date_hierarchy = 'date'

