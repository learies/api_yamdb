from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, GenreViewSet, TitleViewSet, UserViewSet

router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet)
router_v1.register('category', CategoryViewSet)
router_v1.register('genre', GenreViewSet)
router_v1.register('title', TitleViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
