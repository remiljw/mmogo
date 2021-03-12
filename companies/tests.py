from . import views
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from .models import Company, FavoriteList, User
from .serializers import CompanySerializer, FavoriteSerializer





class MmogoAPITests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='foouser', email='user@foo.com', password='@1top_secret')
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        Company.objects.create(name='Mmogo', address='SA', phone_no='01234567')
        Company.objects.create(name='Test PLC', address='Lagos', phone_no='01234567')
        Company.objects.create(name='Mozilla', address='USA', phone_no='01234567')
        Company.objects.create(name='Foodcourt', address='Europe', phone_no='01234567')

    def test_list_companies(self):
        url = reverse('companies:companies')
        request = self.factory.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = views.CompanyView.as_view()(request)
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_add_favorite(self):
        fav = Company.objects.get(name="Mmogo")
        url = 'api/fav/'
        request = self.factory.post(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = views.FavoriteDetailView.as_view()(request, id=fav.pk)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_list_favorite(self):
        self.test_add_favorite()
        url = reverse('companies:favorite')
        request = self.factory.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = views.FavoriteView.as_view()(request)
        favorites = FavoriteList.objects.filter(owner=self.user)
        serializer = FavoriteSerializer(favorites, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    
    def test_delete_favorite(self):
        self.test_add_favorite()
        fav = FavoriteList.objects.get(owner=self.user)
        url = 'api/fav/'
        request = self.factory.delete(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = views.FavoriteDetailView.as_view()(request, id=fav.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
