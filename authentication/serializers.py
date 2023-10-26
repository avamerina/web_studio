from django.contrib.auth import get_user_model
from django.core import exceptions as django_exceptions
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.settings import api_settings
from djoser.serializers import UserCreateSerializer

from utils.helpers import calculate_age


class CustomUserCreateSerializer(UserCreateSerializer):

    def validate(self, attrs):
        User = get_user_model()
        user = User(**attrs)
        password = attrs.get("password")
        birth_date = attrs.get("birth_date")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error[api_settings.NON_FIELD_ERRORS_KEY]}
            )

        if calculate_age(birth_date=birth_date) < 18:
            raise serializers.ValidationError(
                {"birth_date": "User may not be under 18"}
            )

        return attrs


class CustomUserSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['id', 'phone', 'birth_date', 'image', 'age']
        read_only_fields = ['phone', 'age', 'image']

    def get_age(self, obj):
        return calculate_age(obj.birth_date)


class CustomUserPhotoUpdateSerializer(serializers.ModelSerializer):
    image = serializers.CharField(max_length=1000)

    class Meta:
        model = get_user_model()
        fields = ['image']
