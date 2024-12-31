"""Core models for our app."""

from django.contrib.auth.base_user import (
    BaseUserManager,
)
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    """Managers for users."""

    def create_user(
        self, first_name, last_name, email, username, password=None, **extra_fields
    ):
        if not email:
            raise ValueError("User must have an email address.")

        if not username:
            raise ValueError("Username field is required.")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        """Create a new superuser and return superuser"""

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Users in the System"""

    first_name = models.CharField(
        max_length=150,
        blank=True,
        db_index=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        db_index=True,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
    )
    username = models.CharField(
        max_length=50,
        unique=True,
        db_index=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = (
        "first_name",
        "last_name",
        "email",
    )

    class Meta:
        verbose_name = "System User"
        verbose_name_plural = "System Users"
