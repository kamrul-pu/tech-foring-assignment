"""Serializer for user model."""

from django.contrib.auth import get_user_model, authenticate

from rest_framework import status
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
        )
        read_only_fields = ("id",)


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Specify password and confirm_password fields as write_only, meaning they won't be included in responses
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},  # Styling to indicate it's a password field
        trim_whitespace=False,
    )
    confirm_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    # Custom validation for password to check if it matches confirm_password
    def validate_password(self, value):
        password = value
        confirm_password = self.initial_data.get("confirm_password", "")
        if password != confirm_password:
            raise serializers.ValidationError(
                detail="Password and confirm password don't match!!!",  # Error message
                code=status.HTTP_400_BAD_REQUEST,  # HTTP status code
            )
        return value

    class Meta:
        model = User  # Specify the model for the serializer
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "confirm_password",
        )  # Fields to include in the serialization

    # Custom create method to handle user creation
    def create(self, validated_data):
        validated_data.pop(
            "confirm_password", None
        )  # Remove confirm_password from validated data
        user = User(**validated_data)  # Create a new user instance with validated data
        user.set_password(validated_data.get("password", ""))  # Set user's password
        user.save()  # Save the user to the database
        return user  # Return the created user instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    id = serializers.CharField(max_length=15, read_only=True)
    password = serializers.CharField(
        max_length=255,
        write_only=True,
        style={"input_type": "password"},
    )

    def validate(self, attrs):
        username = attrs.get("username", None)
        password = attrs.get("password", None)
        if not username:
            raise serializers.ValidationError(
                detail="An username is required for login",
                code=status.HTTP_400_BAD_REQUEST,
            )
        if not password:
            raise serializers.ValidationError(
                detail="A password is requied for login",
                code=status.HTTP_400_BAD_REQUEST,
            )
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                detail="Invalid Credentials", code=status.HTTP_400_BAD_REQUEST
            )
        if not user.is_active:
            raise serializers.ValidationError(
                detail="User is Inactive", code=status.HTTP_400_BAD_REQUEST
            )
        return {
            "username": user.username,
            "id": user.id,
        }
