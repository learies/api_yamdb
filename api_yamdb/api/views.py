from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from reviews.models import Category, Genre, Title

from .permissions import ExtendedReadOnlyPermission
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer


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


# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
#     # permission_classes = (CustomPermission,)

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

#     def get_queryset(self):
#         rewview = get_object_or_404(Review, id=self.kwargs['review_id'])
#         return review.comments.all()
