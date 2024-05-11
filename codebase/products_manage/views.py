from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import viewsets
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

    def destroy(self, request, pk=None):
        """
        Delete a Product object.
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckLowProductViewSet(GenericViewSet):
    """
    A viewset for checking if a Product has a low quantity.
    """
    LOW_QUANTITY_THRESHOLD = 5  # Configurable threshold
    queryset = []  # Empty queryset

    def get_queryset(self):
        return self.queryset  # Optional: Always return empty queryset

    def check_low_product(self, request):
        """
        Check if a Product has a low quantity based on a configurable threshold.
        """
        product_id = request.query_params.get('product_id')
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)

        if product.quantity < self.LOW_QUANTITY_THRESHOLD:
            return Response({"message": "Low product quantity"})
        else:
            return Response({"message": "Sufficient product quantity"})



class CartItemViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling CRUD operations on CartItem objects.
    """
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific CartItem object by its primary key.
        """
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)
