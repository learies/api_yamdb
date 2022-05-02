from django.db import models


class Category(models.Model):
    """Модель для категории"""
    name = models.CharField(
        max_length=254,
        unique=True,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    """Модель для жанров"""
    name = models.CharField(
        max_length=254,
        unique=True,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )

    def __str__(self) -> str:
        return self.name


class Title(models.Model):
    """Модель для произведений"""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category',
    )
    genre = models.ManyToManyField(
        'Genre',
        related_name='genre',
    )
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name
