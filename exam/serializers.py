from rest_framework.serializers import ModelSerializer
from .models import Exam, Question, Course


class ExamSerializer(ModelSerializer):
    """ serializer for exam """

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

