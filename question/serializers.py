from rest_framework import serializers
from question.models import Question, Option
from django.utils import timezone


class OptionSerializer(serializers.ModelSerializer):
    """serializer for option """
    class Meta:
        model = Option
        fields = ['text']


class QuestionSerializer(serializers.ModelSerializer):
    """ serializer for question """
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id','text', 'answer', 'options']

    def create(self, validated_data):
        options = validated_data.pop('options')
        question = Question.objects.create(**validated_data)
        for opt in options:
            Option.objects.create(question=question, **opt)

        return question

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.answer = validated_data.get('answer', instance.answer)
        instance.created_by = validated_data.get(
            'created_by', instance.created_by)
        instance.created = timezone.now()
        instance.save()

        options_data = validated_data.pop('options')
        options = instance.options.all()
        for index, opt in enumerate(options_data):
            option = options[index]
            option.text = opt.get('text', option.text)
            option.save()

        return instance


class QuestionResponseSerializer(serializers.ModelSerializer):
    """ serializer for question resposne"""

    options = OptionSerializer(many=True)
    class Meta:
        model = Question
        fields = "__all__"
    



