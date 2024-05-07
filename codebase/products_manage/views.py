from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from django.core.exceptions import ObjectDoesNotExist
from .utility import send_reorder_alert

class ProductList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductDetail(APIView):
    # permission_classes = [IsAuthenticated]

    def get_product(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_product(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_product(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        product = self.get_product(pk)
        product.delete()
        return Response(status=204)  # No content returned on successful deletion

    @staticmethod
    def update_stock(product_id, quantity):
        try:
            product = Product.objects.select_for_update().get(id=product_id)
        except ObjectDoesNotExist:
            raise ValueError("Product not found")

        product.stock += quantity
        product.save()

        if product.stock_quantity < product.reorder_point:
            send_reorder_alert(product)
