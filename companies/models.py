from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email,  password, **extra_fields):
        '''
        Create and return a `User` with superuser (admin) permisissions.
        '''
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(username, email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserAccountManager()

    def __str__(self):
        return self.email
    

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = ("Companies")

    def __str__(self):
        return self.name

class FavoriteList(models.Model):
    owner = models.ForeignKey("User",  on_delete=models.CASCADE)
    company = models.ForeignKey("Company",  on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ("Favorite Lists")

    def __str__(self):
        return str(self.owner)
    
    # def get_absolute_url(self):
    #     return reverse("FavoriteList_detail", kwargs={"pk": self.pk})