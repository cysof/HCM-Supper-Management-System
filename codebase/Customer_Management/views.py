from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import CustomUserSerializer, PurchesSerializer, OrderSerializer, OrderItemSerializer
from .models import CustomUser, Purches, Order, OrderItem
from django.db.models import Sum

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    """
    API endpoint that allows users to be created.
    """
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        """
        Handles the HTTP POST request to create a new authentication token for a user.

        Parameters:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the generated token.

        Raises:
            ValidationError: If the serializer fails to validate the request data.

        """
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to view and update their profile.
    """
    serializer_class = CustomUserSerializer

    def get_object(self):
        """
        Retrieves and returns the user object associated with the current request.
        """
        return self.request.user
    
class PurchesViewSet(viewsets.ModelViewSet):
    queryset = Purches.objects.all()
    serializer_class = PurchesSerializer

    def total_purchase_amount(self, request, customer_id):
        total_amount = Purches.objects.filter(customer_id=customer_id).aggregate(total_amount=Sum('price__amount'))['total_amount']
        return Response({'customer_id': customer_id, 'total_purchase_amount': total_amount})

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