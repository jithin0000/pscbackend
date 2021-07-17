from django.db import models
from agent.models import Agent
from student.models import Student

# Create your models here.
course_choices = [
    ('CREATED','CREATED'),
    ('STARTED','STARTED'),
    ('ENDED','ENDED'),
    ('SUSPENDED','SUSPENDED'),
]

class Course(models.Model):
    """ model for course """  
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(Agent, related_name='created_courses', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(choices=course_choices, max_length=50)
    students = models.ManyToManyField(Student, null=True)

    # rating
    # exams
