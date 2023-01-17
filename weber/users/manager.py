from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
	def _create_user(self, username, password, **extra_fields):
		if not username:
			raise ValueError("The username cannot be blank")

		user = self.model(username=username, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_user(self, username, password=None, **extra_fields):
		return self._create_user(username, password, **extra_fields)

	def create_superuser(self, username, password, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault("is_active", True)

		if not extra_fields.get("is_staff"):
			raise ValueError("Superuser must have is_staff set to True")
		if not extra_fields.get("is_superuser"):
			raise ValueError("Superuser must have is_superuser set to True")
		return self.create_user(username, password, **extra_fields)
