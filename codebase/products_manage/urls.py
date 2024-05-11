from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import CheckLowProductViewSet, ProductViewSet, CartItemViewSet

router = DefaultRouter()

custom_router = SimpleRouter()
custom_router.register(r'check-stock', CheckLowProductViewSet, basename='check-stock')

router.register(r'cart-items', CartItemViewSet)
router.register(r'products', ProductViewSet, basename='product')

# Include the CheckLowProductViewSet with the desired prefix
urlpatterns = [
    path('', include(router.urls)),  # Include the default router URLs for cart-items and products
    path('custum', include(custom_router.urls)),  # Include the custom router URLs
]
