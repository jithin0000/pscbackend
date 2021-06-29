from django.db import models
from django.conf import settings

# Create your models here.


class Agent(models.Model):
    """ model for agent"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)

    address_state = models.CharField(max_length=255)
    address_city = models.CharField(max_length=255)
    address_pin = models.CharField(max_length=6)

    def __str__(self):
        return self.user.email+"__"+self.name
