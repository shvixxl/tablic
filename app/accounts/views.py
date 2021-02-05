from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import RegisterUserSerializer


class RegisterUserView(CreateAPIView):
    """API view for creating new User"""
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer
