from django.db import models
from question.models import Question
from agent.models import Agent

# Create your models here.

class QuestionPaper(models.Model):
    """Model definition for QuestionPaper."""

    title = models.CharField( max_length=255)
    questions = models.ManyToManyField(Question,through='QuestionPaperQuestion')
    added_by = models.ForeignKey(Agent, on_delete=models.CASCADE)
    created = models.DateTimeField( auto_now_add=True)

    class Meta:
        """Meta definition for QuestionPaper."""

        verbose_name = 'QuestionPaper'
        verbose_name_plural = 'QuestionPapers'

    def __str__(self):
        """Unicode representation of QuestionPaper."""
        return self.title


class QuestionPaperQuestion(models.Model):
    """ model question paper and question """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_paper = models.ForeignKey(QuestionPaper,on_delete=models.CASCADE)
    time_taken = models.IntegerField(null=True,blank=True)
    user_answer = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self) -> str:
        return self.question_paper.title

