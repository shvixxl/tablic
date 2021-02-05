from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import User
from .services import create_user


class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for custom User model"""

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return create_user(**validated_data)

    def validate_password(self, value):
        """Validate Password field with Django password validation"""
        try:
            validate_password(password=value)
        except ValidationError as error:
            raise serializers.ValidationError(list(error.messages))
        return value

    
