from django.http import request
from .serializers import QuestionSerializer, OptionSerializer, Question, Option
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import QuestionSerializer
from customauth.permissions import AgentOnly
from agent.models import Agent
# Create your views here.


class BaseQuestionView():
    permission_classes = [IsAuthenticated, AgentOnly]
    authentication_classes = [TokenAuthentication]


class QuestionCreateView(BaseQuestionView, CreateAPIView):
    """ question create api view """
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        agent = Agent.objects.get(user=self.request.user)
        serializer.save(created_by=agent)

# update question


class QuestionUpdateView(BaseQuestionView, UpdateAPIView):
    """ view for updating question with options """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


# get question
# delete question
