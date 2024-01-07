from django.contrib import admin
from .models import (
    Tag,
    Recipe,
    Ingredient
)
# Register your models here...


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title", )
    list_display_links = ("id", 'title')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientInline, )
    list_display = ('id', 'title', 'author', "created_date")
    search_fields = ("title", "author__username")
    list_filter = ('created_date',)
    autocomplete_fields = ('author', )
    date_hierarchy = 'created_date'
    filter_horizontal = ('tag', )
    list_display_links = ("id", 'title')
    readonly_fields = ('slug', 'created_date')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "recipe", 'title', 'quantity', 'unit', "is_active")
    search_fields = ('recipe__title', 'title')
    list_filter = ('is_active', 'unit')
    list_display_links = ("id", 'title')
    autocomplete_fields = ('recipe', )
