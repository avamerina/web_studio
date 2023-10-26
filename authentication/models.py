from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from authentication.managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    phone = PhoneNumberField(unique=True)
    birth_date = models.DateField()
    image = models.CharField(max_length=1000)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['birth_date']

    objects = CustomUserManager()

    def __str__(self):
        return self.phone
