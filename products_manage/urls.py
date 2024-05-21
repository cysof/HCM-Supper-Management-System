from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
#from Customer_Management.views import CustomUserViewSet, UserCreateAPIView

from .views import (ProductViewSet, 
                    CartItemViewSet, 
                    OrderViewSet, 
                    OrderItemViewSet, 
                    CategoryViewSet
)

router = DefaultRouter()

custom_router = SimpleRouter()


# custom_router.register(r'check-stock', CheckLowProductViewSet, basename='check-stock')

router.register(r'category', CategoryViewSet, basename='category')
router.register(r'cart-items', CartItemViewSet, basename='cart-items')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'order-items', OrderItemViewSet, basename='order-items')
#router.register(r'create-user', UserCreateAPIView, basename='create-user')
#router.register(r'users', CustomUserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),

    #path('', CategoryViewSet.as_view({'get': 'check_low_product_detail'}), name='category'),
    path('api/products/<int:pk>/check_low_product/', ProductViewSet.as_view({'get': 'check_low_product'}), name='product-check-low-product-detail'),
    path('api/cart-items/calculate-total-cost/', CartItemViewSet.as_view({'get': 'calculate_total_cost'}), name='calculate-total-cost'),
 #   path('api/create-user/', UserCreateAPIView.as_view({'post': 'create'}), name='user-create'),
    #path('custom/', include(custom_router.urls)),
    
    
]
