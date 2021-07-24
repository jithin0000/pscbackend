from django.db import models

from agent.models import Agent
from course.models import Course
from question.models import Question
# Create your models here.
exam_status = [
    ("CREATED", 'CREATED'),
    ("STARTED", 'STARTED'),
    ("ENDED", 'ENDED'),
    ("SUSPENDED", 'SUSPENDED'),
]


class Exam(models.Model):
    """ model for exam """
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_questions = models.IntegerField(default=0)
    mark_per_question = models.IntegerField(default=1)
    minus_mark_per_question = models.IntegerField(default=-1)
    status = models.CharField(choices=exam_status, default="CREATED", max_length=50)
    course = models.ForeignKey(Course, related_name="exams", null=True, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, related_name="exam",null=True)
    created_by = models.ForeignKey(Agent, related_name="exam_list",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
