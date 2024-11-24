from django.contrib import admin

from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
