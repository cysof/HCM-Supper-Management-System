from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomUserViewSet, 
    UserCreateAPIView, 
    CustomAuthToken, 
    UserProfileAPIView, 
    
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api-token-auth'),
    path('users/profile/', UserProfileAPIView.as_view(), name='user-profile'),

]

urlpatterns += router.urls