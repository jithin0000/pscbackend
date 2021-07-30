from customauth.models import MyUser
from agent.models import Agent
from question import models
from question.models import Question,Option
from student.models import Student
from faker import Faker
fake = Faker()

from django.utils import timezone
from django.utils.timezone import timedelta

""" assumes that agent with agent@gmail.com exist """

def generate_students():
    """ generate fake students """
    Student.objects.create(
        owner = MyUser.objects.create_user(
            email =fake.email(),
            password ="testpassword",
        ),
        name = fake.name(),
        phone_number = fake.phone_number(),
        added_by = MyUser.objects.get(email="newagent@gmail.com"),
        created = timezone.now()
    )


def simulate():
    for i in range(100):
        generate_students()