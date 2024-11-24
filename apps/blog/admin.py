from django.contrib import admin

from .models import (
    Article,
    Description,
    Comment
)
class DescriptionAdmin(admin.TabularInline):
    model = Description
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [DescriptionAdmin]
    list_display = ('id', 'title', 'owner', 'created_date')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'owner')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_date')
    list_display_links = ('id', 'name')
    paginator = 10


