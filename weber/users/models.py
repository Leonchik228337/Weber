from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
	email = None
	username = models.CharField(max_length=50, unique=True, verbose_name="Имя пользователя")
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)

	objects = CustomUserManager()

	USERNAME_FIELD = "username"
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.username
