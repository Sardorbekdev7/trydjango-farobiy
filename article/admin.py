from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'slug', 'modified_at', 'created_at')
    list_display_links = ('id', 'title')
    readonly_fields = ('slug', 'modified_at', 'created_at')
    ordering = ('id', )
    # prepopulated_fields = {"slug": {"title", }}


admin.site.register(Article, ArticleAdmin)
