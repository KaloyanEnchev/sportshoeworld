from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from accounts.managers import AppUserManager
from common.vaidators import validate_image_size


# Create your models here.
class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"

    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = AppUserManager()

    def __str__(self) -> str:
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to='post_images/',
        blank=True,
        null=True,
        validators=[
            validate_image_size
        ]
    )
    @property
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"