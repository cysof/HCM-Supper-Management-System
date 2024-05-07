from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, UserCreateAPIView, CustomAuthToken, UserProfileAPIView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    # Include the URLs generated by the router
    path('', include(router.urls)),
    
    # URL for user creation
    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
    
    # URL for custom authentication token
    path('auth/token/', CustomAuthToken.as_view(), name='custom-auth-token'),

    # URL for user profile
    path('users/profile/', UserProfileAPIView.as_view(), name='user-profile'),
]