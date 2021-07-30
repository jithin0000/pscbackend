import random
from agent.models import Agent
from course.models import Course
from customauth.models import MyUser
from django.utils import timezone
from django.utils.timezone import timedelta
from faker import Faker
from question import models
from question.models import Option, Question
from student.models import Student

fake = Faker()


""" assumes that agent with agent@gmail.com exist """


def generate_students():
    """ generate fake students """
    Student.objects.create(
        owner=MyUser.objects.create_user(
            email=fake.email(),
            password="testpassword",
        ),
        name=fake.name(),
        phone_number=fake.phone_number(),
        added_by=MyUser.objects.get(email="newagent@gmail.com"),
        created=timezone.now()
    )

statuses = ['CREATED','ENDED','SUSPENDED','STARTED']

def generate_fake_course(index):
    delta = index % 30
    if delta < 1:
        delta = 1
    status =statuses[random.randint(0,3)]

    Course.objects.create(
        title=fake.job(),
        created_by=Agent.objects.get(user__email="newagent@gmail.com"),
        start_time=timezone.now() + timedelta(delta),
        end_time=timezone.now() + timedelta(20),
        status = status,
    )


def simulate_course():
    for i in range(1, 100):
        generate_fake_course(i)
