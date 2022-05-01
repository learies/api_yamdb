from django.contrib import admin

from .models import Category, Genre, Title


class TitleAdmin(admin.ModelAdmin): 
    list_display = ('name', 'category','year') 
    list_filter = ('genre',) 
    empty_value_display = '-пусто-'

admin.site.register(Title, TitleAdmin) 
admin.site.register(Category) 
admin.site.register(Genre) 
 
