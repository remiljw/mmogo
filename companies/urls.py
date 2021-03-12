from django.urls import path, re_path

from . import views

app_name = 'companies'

urlpatterns = [
    re_path('user/activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.UserActivationView.as_view(), name='activate'),
    re_path('password/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.ResetPasswordView.as_view(), name='reset'),
    path('companies/', views.CompanyView.as_view(), name='companies'),
    path('favorites/', views.FavoriteView.as_view(), name='favorite'),
    path('fav/<int:id>', views.FavoriteDetailView.as_view(), name='detail'),
    # path('add/<int:id>', views.AddFavorite.as_view(), name = 'add')
 
]
