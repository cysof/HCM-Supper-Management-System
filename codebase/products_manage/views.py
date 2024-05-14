from django.shortcuts import get_object_or_404
from django.urls import reverse

from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status

from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling CRUD operations on Product objects.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        """
        List all Product objects.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific Product object by its primary key.
        """
        try:
            instance = self.get_object()
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new Product object.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update an existing Product object.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def check_low_product(self, request, product_id):
        quantity_threshold = 5
        product = get_object_or_404(Product, id=product_id)
        if product.stock_quantity < quantity_threshold:
            return Response({"message": "Low product quantity"})
        else:
            return Response({"message": "Sufficient product quantity"})

    @action(methods=['GET'], detail=True)
    def check_low_product_detail(self, request, pk=None):
        return self.check_low_product(request, pk)

    def destroy(self, request, pk=None):
        """
        Delete a Product object.
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartItemViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling CRUD operations on CartItem objects.
    """
    serializer_class = CartItemSerializer

    def get_queryset(self):
        queryset = CartItem.objects.all()
        return queryset

    def calculate_total_price(self, cart_items):
        """
        Calculate the total price of items in the cart.
        """
        total_price = 0
        for cart_item in cart_items:
            total_price += cart_item.product.price * cart_item.quantity
        return total_price

    def list(self, request):
        cart_items = self.get_queryset()
        return Response(CartItemSerializer(cart_items, many=True).data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        cart_item = self.get_object()
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_200_OK)

    def calculate_total_price(self, request):
        cart_items = self.get_queryset()
        total_price = self.calculate_total_price(cart_items)
        return Response({'total_price': total_price}, status=status.HTTP_200_OK)
