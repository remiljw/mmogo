from django.urls import path

from . import views

app_name = 'companies'

urlpatterns = [
    path('companies/', views.CompanyView.as_view(), name='companies'),
    path('favorites/', views.FavoriteView.as_view(), name='favorite'),
    path('fav/<int:id>', views.FavoriteDetailView.as_view(), name='detail'),
    # path('add/<int:id>', views.AddFavorite.as_view(), name = 'add')
 
]
