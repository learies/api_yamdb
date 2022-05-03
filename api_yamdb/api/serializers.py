from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Category, Genre, Title
from users.models import User
from django.db.models import Sum,Avg,Max,Min,Count,F,Q


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'id',
            'first_name',
            'last_name',
            'email',
            'role',
            'bio',
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        required=False,
        queryset=Genre.objects.all()
    )

    # avgrating = serializers.SerializerMethodField()

    # def get_avgrating(self, obj):
    #     avgrating = Title.objects.aggregate(Avg('rating'))['rating__avg']
    #     return avgrating

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'category', 'genre', 'rating')
