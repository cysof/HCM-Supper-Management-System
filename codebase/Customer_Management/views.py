from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import CustomUserSerializer
from .models import CustomUser

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