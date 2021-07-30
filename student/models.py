from django.db import models
from customauth.models import MyUser
# Create your models here.


class Student(models.Model):
    """ model for student """
    owner = models.OneToOneField(MyUser, related_name='user_owner',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    profile_pic_url = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=12)
    # need to fix this
    added_by = models.ForeignKey(
        MyUser, on_delete=models.SET_NULL, null=True, related_name="agent_students")

    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    # need to add courses
