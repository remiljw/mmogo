from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Company, FavoriteList

# Register your models here.

admin.site.register(User)
admin.site.register(Company)
admin.site.register(FavoriteList)

admin.site.unregister(Group)