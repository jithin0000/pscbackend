from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, role=None, password=None):
        if not email:
            raise ValueError("user must have an email address")

        if role == None:
            role = "STUDENT"

        user = self.model(
            email=self.normalize_email(email),
            role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password, role='ADMIN')
        user.is_admin = True
        user.save(using=self._db)
        return user


user_role_choices = [
    ('ADMIN', 'ADMIN'),
    ('AGENT', 'AGENT'),
    ('STUDENT', 'STUDENT'),

]


class MyUser(AbstractBaseUser):
    """ custom user model """

    email = models.EmailField(verbose_name="email address",
                              max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(choices=user_role_choices,
                            default='STUDENT', max_length=125)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
