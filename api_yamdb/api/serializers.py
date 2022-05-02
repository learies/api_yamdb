from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Title, Category, Genre


class TitleSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field="name", read_only=True)
    # genre = SlugRelatedField(slug_field="name", read_only=True)
    # genre = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'category', 'genre')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', 'slug',)