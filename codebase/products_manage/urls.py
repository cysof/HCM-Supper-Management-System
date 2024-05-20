from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import ProductViewSet, CartItemViewSet, OrderViewSet, OrderItemViewSet, CategoryViewSet

router = DefaultRouter()

custom_router = SimpleRouter()
# custom_router.register(r'check-stock', CheckLowProductViewSet, basename='check-stock')

router.register(r'category', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

router.register(r'cart-items', CartItemViewSet, basename='cart-items')

router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'order-items', OrderItemViewSet, basename='order-items')

# Include the CheckLowProductViewSet with the desired prefix
urlpatterns = [
    path('', include(router.urls)),  # Include the default router URLs for cart-items and products

    path('category/', CategoryViewSet.as_view({'get': 'check_low_product_detail'}), name='category'),
    path('products/<int:pk>/check_low_product/', ProductViewSet.as_view({'get': 'check_low_product'}), name='product-check-low-product-detail'),

    path('custom/', include(custom_router.urls)),  # Include the custom router URLs
    
    path('cart-items/calculate-total-cost/', CartItemViewSet.as_view({'get': 'calculate_total_cost'}), name='calculate-total-cost'),
]