from django.shortcuts import get_object_or_404
from django.urls import reverse

from rest_framework import status
from rest_framework import generics, status, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi 


from .models import Product, CartItem, Order, OrderItem, Category
from .serializers import (ProductSerializer,
                          CartItemSerializer,
                          OrderSerializer,
                          OrderItemSerializer,
                          CategorySerializer
                          )


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['GET'])
    def check_low_product(self, request, pk=None):
        quantity_threshold = 5
        product = get_object_or_404(Product, pk=pk)
        if product.stock_quantity < quantity_threshold:
            return Response({"message": "Low product quantity"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Sufficient product quantity"}, status=status.HTTP_200_OK)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['GET'])
    def check_low_product_detail(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        low_stock_products = category.products.filter(stock_quantity__lt=5)
        
        if low_stock_products.exists():
            product_names = ", ".join([product.name for product in low_stock_products])
            return Response(
                {"message": f"The following products have low stock: {product_names}"},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "All products have sufficient stock"},
                status=status.HTTP_200_OK
            )

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


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        """
        Handles the HTTP POST request to create an order for a user.

        Parameters:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the created order.

        Raises:
            ValidationError: If the serializer fails to validate the request data.

        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(user=user)
        return Order.objects.none()

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):
        """
        Handles the HTTP POST request to create an order item for an order.

        Parameters:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the created order item.

        Raises:
            ValidationError: If the serializer fails to validate the request data.

        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        """
        Handles the HTTP PUT request to update an order item for an order.

        Parameters:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the updated order item.

        Raises:
            ValidationError: If the serializer fails to validate the request data.

        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        """
        Handles the HTTP DELETE request to delete an order item for an order.

        Parameters:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the deleted order item.

        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@swagger_auto_schema(
    operation_id='get_products',
    tags=['Products'],
    responses={200: openapi.Response(description='List of products')},
)
def get_products(request):
    # Your view logic for getting products
    return Response()