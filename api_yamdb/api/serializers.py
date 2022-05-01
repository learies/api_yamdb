from rest_framework import serializers
from reviews.models import Title, Category, Genre


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name')

    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name')

    class Meta:
        model = Genre
        fields = '__all__'