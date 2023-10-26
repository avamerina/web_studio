from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

router = DefaultRouter()
router.register('profiles', CustomUserViewSet, basename='profile')

urlpatterns += router.urls
