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

    genre = SlugRelatedField(slug_field="name", queryset=Genre.objects.all())
    # genre = SlugRelatedField(slug_field="name", queryset=Genre.objects.get(id=1))
    print('===============================================================')
    # print('category=', category)  
    # print('genre=', genre)
    print('===============================================================')
 

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'category', 'genre')
