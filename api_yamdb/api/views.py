from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg

from reviews.models import Category, Genre, Title
from users.models import User

from .permissions import ExtendedReadOnlyPermission
from .serializers import (CategorySerializer, GenreSerializer, MeSerializer,
                          TitleSerializer, UserSerializer, ReviewSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('username')
    search_fields = ('username',)

    @action(
        methods=['get', 'patch'],
        detail=False,
        url_path='me',
    )
    def me(self, request):
        user = get_object_or_404(User, username=self.request.user)
        if request.method == 'GET':
            serializer = MeSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = MeSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (ExtendedReadOnlyPermission,)
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = (ExtendedReadOnlyPermission,)
    serializer_class = GenreSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        serializer.save(author=self.request.user, title=title)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = (ExtendedReadOnlyPermission,)
    serializer_class = TitleSerializer

    def perform_create(self, serializer):
        rating = Title.objects.values('rating').aggregate(avg_rating=Avg('rating'))
        print('======================================================================================')
        print('rating=', rating)
        print('======================================================================================')
 
        serializer.save()
        # serializer.save(rating=avg_rating)