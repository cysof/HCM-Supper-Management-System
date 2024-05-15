from django.shortcuts import get_object_or_404
from django.urls import reverse

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi 


from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Other CRUD operations for Product objects
    
    def check_low_product(self, request, product_id):
        quantity_threshold = 5
        product = get_object_or_404(Product, id=product_id)
        if product.stock_quantity < quantity_threshold:
            return Response({"message": "Low product quantity"})
        else:
            return Response({"message": "Sufficient product quantity"})

    @action(detail=True, methods=['GET'])
    def check_low_product_detail(self, request, pk=None):
        return self.check_low_product(request, pk)

    # Other methods for ProductViewSet

class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def calculate_total_cost(self, request):
        """
        Calculate the total cost of items in the cart and return the total cost in a Response object.
        """
        cart_items = self.get_queryset()
        total_cost = sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)
        return Response({'total_cost': total_cost}, status=status.HTTP_200_OK)

    def list(self, request):
        cart_items = self.get_queryset()
        return Response(CartItemSerializer(cart_items, many=True).data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        cart_item = self.get_object()
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_200_OK)

    # Other CRUD operations for CartItem objects

@api_view(['GET'])
@swagger_auto_schema(
    operation_id='get_products',
    tags=['Products'],
    responses={200: openapi.Response(description='List of products')},
)
def get_products(request):
    # Your view logic for getting products
    return Response()