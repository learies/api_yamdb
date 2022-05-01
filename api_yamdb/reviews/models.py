from django.db import models


class Category(models.Model):
    """Модель для категории"""
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name
