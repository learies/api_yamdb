from django.contrib import admin

from .models import Category, Genre, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'year', 'description')
    list_filter = ('genre',)
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
