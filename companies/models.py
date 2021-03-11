from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password, **extra_fields):
        '''
        Create and return a `User` with superuser (admin) permisissions.
        '''
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, password, is_superuser=True)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def __str__(self):
        return self.email

class Company(models.Model):
    name = models.Charfield(max_length=255)
    address = models.Charfield(max_length=255)
    phone_number = models.Charfield(max_length=255)

    

    # class Meta:
    #     verbose_name = _("Company")
    #     verbose_name_plural = _("Company")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Company _detail", kwargs={"pk": self.pk})

class FavoriteList(models.Model):
    owner = models.OneToOneField("User", verbose_name=_(""), on_delete=models.CASCADE)
    company = models.models.ForeignKey("Company", verbose_name=_(""), on_delete=models.CASCADE)

    

    # class Meta:
    #     verbose_name = _("FavoriteList")
    #     verbose_name_plural = _("FavoriteList")

    def __str__(self):
        return self.owner

    # def get_absolute_url(self):
    #     return reverse("FavoriteList_detail", kwargs={"pk": self.pk})
)