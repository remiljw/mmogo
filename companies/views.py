from django.shortcuts import render
from rest_framework import generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company, FavoriteList, User
from .serializers import CompanySerializer, FavoriteSerializer
from django.shortcuts import get_object_or_404

class CompanyView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']


class FavoriteView(generics.ListAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        favorites = FavoriteList.objects.filter(owner=self.request.user)
        return favorites
        
class FavoriteDetailView(APIView):
    def post(self, request, id, format=None):
        # user = User.objects.get(email='remi@remi.com')
        com =  get_object_or_404(Company, id=id)
        company = FavoriteList.objects.create(owner=user, company_id=id)
        # print(company)
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