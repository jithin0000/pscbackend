from django.db import models
from agent.models import Agent
# Create your models here.


class Question(models.Model):
    """model for question"""

    text = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        Agent, on_delete=models.CASCADE, related_name="created_questions")
    answer = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return self.text


class Option(models.Model):
    """option for question ."""
    text = models.CharField(max_length=255)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options")

    class Meta:
        """Meta definition for Option."""

        verbose_name = 'Option'
        verbose_name_plural = 'Options'

    def __str__(self):
        """Unicode representation of Option."""
        return self.text
