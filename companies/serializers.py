from rest_framework import serializers
from django.contrib.auth.models import update_last_login
from .models import Company, FavoriteList
from django.contrib.auth import get_user_model, authenticate
# from rest_framework_jwt.settings import api_settings
from django.shortcuts import get_object_or_404


# User = get_user_model()
# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


# class SignUpSerializer(serializers.ModelSerializer): 
#     password = serializers.CharField(max_length=128, min_length=8, write_only=True)
#     class Meta: 
#         model = User
#         fields = ('email', 'password',)

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)

#     def validate(self, data):
#         email = data.get("email", None)
#         password = data.get("password", None)
#         user = authenticate(email=email, password=password)
#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email and password is not found.'
#             )
#         try:
#             payload = JWT_PAYLOAD_HANDLER(user)
#             jwt_token = JWT_ENCODE_HANDLER(payload)
#             update_last_login(None, user)
#         except User.DoesNotExist:
#             raise serializers.ValidationError(
#                 'User with given email and password does not exists'
#             )
#         return {
#             'email':user.email,
#             'token': jwt_token
#         }

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = ('id','company',)
        depth = 1 