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
        

    
