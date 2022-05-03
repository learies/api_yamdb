from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Title, Category, Genre


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', 'slug',)


class TitleSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())
    genre = serializers.SlugRelatedField(slug_field='name', many=True, queryset=Genre.objects.all())

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'category', 'genre')
