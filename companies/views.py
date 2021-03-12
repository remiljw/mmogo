import requests
from django.shortcuts import render
from rest_framework import generics, filters, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Company, FavoriteList, User
from .serializers import CompanySerializer, FavoriteSerializer
from django.shortcuts import get_object_or_404


class UserActivationView(APIView):
    permission_classes = (AllowAny,)
    def get (self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data = post_data)
        content = result.json()
        return Response(content)

class ResetPasswordView(APIView):
    permission_classes = (AllowAny,)
    def get (self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        new_password = request.data.get('new_password')
        post_url = web_url + "/auth/users/reset_password_confirm/"
        post_data = {'uid': uid, 'token': token, 'new_password': new_password }
        result = requests.post(post_url, data = post_data)
        content = result.json()
        return Response(content)
    

class CompanyView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']


class FavoriteView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        favorites = FavoriteList.objects.filter(owner=self.request.user)
        return favorites
        
class FavoriteDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, id, format=None):
        com =  get_object_or_404(Company, id=id)
        company = FavoriteList.objects.create(owner=request.user, company_id=id)
        response = {
            'message' : '{} is added to favorites'.format(company.company)
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def delete(self, request, id, format=None):
        company = get_object_or_404(FavoriteList, id=id)
        company.delete()
        response = {
            'message' : company.company.name + ' is removed from favorites'
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)