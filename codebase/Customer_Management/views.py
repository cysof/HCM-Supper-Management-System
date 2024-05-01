from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Purches, CustomerBio
from .serializers import CustomerBioSerializer, PurcheSerializer


class CustomerBioList(APIView):
    #permission_classes = [IsAuthenticated]


    def get(self, request):
        customerBio = CustomerBio.objects.all()
        serializer = CustomerBioSerializer(customerBio, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomerBioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class CustomerBioDetail(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        customerBio = get_object_or_404(CustomerBio, pk=pk)
        serializer = CustomerBioSerializer(customerBio)
        return Response(serializer.data)
    
    def put(self, request, pk):
        customerBio = get_object_or_404(CustomerBio, pk=pk)
        serializer = CustomerBioSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        customerBio = get_object_or_404(CustomerBio, pk=pk)
        customerBio.delete()
        return Response(status=204)

class PurchesList(APIView):
    #permission_classes = [IsAuthenticated]  # Uncomment for authentication
    """this view handle the list of all the purches a cutomer made"""

    def get(self, request):
        purches = Purches.objects.all()
        serializer = PurcheSerializer(purches, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurcheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PurchesDetail(APIView):
    """This view handle detail of all purche"""

    def get(self, request, pk):
        purches = get_object_or_404(Purches, pk=pk)
        serializer = PurcheSerializer(purches)
        return Response(serializer.data)

    def put(self, request, pk):
        purches = get_object_or_404(Purches, pk=pk)
        serializer = PurcheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        purches = get_object_or_404(Purches, pk=pk)
        purches.delete()
        return Response(status=204)
    
