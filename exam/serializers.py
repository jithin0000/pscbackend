from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField
from .models import Exam, Question, Course
from question.serializers import QuestionResponseSerializer

class ExamSerializer(ModelSerializer):
    """ serializer for exam """
    questions = PrimaryKeyRelatedField(many=True,queryset=Question.objects.all())
    class Meta:
        model = Exam
        fields = ['id','name','start_time', 'end_time', 'total_questions',
        'mark_per_question','minus_mark_per_question','questions',
        'course']



class ExamResponseSerializer(ModelSerializer):
    """ serializer for exam """

    class Meta:
        model = Exam
        fields = "__all__"

class ExamDetailSerializer(ModelSerializer):
    """ serializer for exam details"""
    questions = PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = Exam
        fields ="__all__"
