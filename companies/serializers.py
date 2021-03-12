from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import Company, FavoriteList
from django.contrib.auth import get_user_model



User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('username', 'email', 'password',)
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = ('id','company',)
        depth = 1 