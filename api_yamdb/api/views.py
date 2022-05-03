from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, serializers
from django.db.models import Avg

from reviews.models import Category, Genre, Title
from users.models import User

from .permissions import ExtendedReadOnlyPermission
from .serializers import (CategorySerializer, GenreSerializer, TitleSerializer,
                          UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (ExtendedReadOnlyPermission,)
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = (ExtendedReadOnlyPermission,)
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = (ExtendedReadOnlyPermission,)
    serializer_class = TitleSerializer

    # def perform_create(self, serializer):
    #     rating = Title.objects.values('rating').aggregate(avg_rating=Avg('rating'))
    #     print('======================================================================================')
    #     print('rating=', rating)
    #     print('======================================================================================')
 
        # serializer.save
        # serializer.save(rating=avg_rating)


