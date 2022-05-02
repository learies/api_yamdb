from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        now = timezone.now()
        if not username:
            raise ValueError('Введите имя/логин.')
        if not email:
            raise ValueError('Введите email.')
        if not password:
            raise ValueError('Введите пароль.')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            last_login=now,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
