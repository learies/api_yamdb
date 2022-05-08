from django.contrib import admin

from .models import User


@admin.register(User)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
<<<<<<< HEAD
        'id', 'username', 'first_name', 
        'last_name', 'email', 'role',
=======
        'id', 'username', 'first_name', 'last_name', 'email', 'role'
>>>>>>> 5be3b688b156641494248063d7b7ca82f7606192
    )
