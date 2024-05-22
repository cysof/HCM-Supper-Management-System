from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny


from django.contrib.auth.password_validation import validate_password



from .models import CustomUser


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Default permission for all actions


    def has_permission(self, request, view):
        """
        Override has_permission to explicitly pass the view.
        """
        if self.action in ('create',):
            return True  # Allow anyone to create users
        return IsAuthenticated.has_permission(self, request, view)

    def create(self, request):
        """
        Override create to validate password and create user.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data['password']

        # Validate password before creating user
        try:
            validate_password(password)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        user = serializer.instance
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """
        Override update to allow updating user information.
        """
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        Override destroy to delete the user.
        """
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
