from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserRole(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        # if not phone_number:
        #     raise ValueError('Users must have an phone_number')

        user = self.model(
            email=self.normalize_email(email),

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    objects        = UserManager()
    email          = models.CharField(max_length=254, null=True, blank=True, unique=True)
    username       = models.CharField(max_length=254, null=True, blank=True)
    first_name     = models.CharField(max_length=256, blank=True, null=True)
    last_name      = models.CharField(max_length=256, blank=True, null=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):

        if self.email:
            return str(self.email)
        else:
            "NA"