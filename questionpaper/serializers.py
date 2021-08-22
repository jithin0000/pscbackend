from rest_framework import serializers
from .models import QuestionPaperQuestion, QuestionPaper,Question
from question.serializers import QuestionResponseSerializer, QuestionSerializer

class QuestionPaperSerializer(serializers.ModelSerializer):
    """ serializer for question """
    questions=serializers.PrimaryKeyRelatedField(many=True,queryset=Question.objects.all())
    class Meta:
        model = QuestionPaper
        fields = ['title','questions']



class QuestionPaperResponseSerializer(serializers.ModelSerializer):
    """ serializer for question """
    questions=QuestionSerializer(many=True)
    class Meta:
        model = QuestionPaper
        fields = "__all__"



class QuestionPaperQuestionSerializer(serializers.ModelSerializer):
    """serializer for question paper serializer"""
    class Meta:
        model = QuestionPaperQuestion
        fields = "__all__"

class QuestionPaperQuestionResponseSerializer(serializers.ModelSerializer):
    """serializer"""
    question_paper=QuestionPaperSerializer()
    class Meta:
        model=QuestionPaperQuestion
        fields="__all__"

