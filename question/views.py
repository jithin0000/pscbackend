from rest_framework.views import APIView
from fileupload.models import FileUpload
from django.http import request
from .serializers import QuestionResponseSerializer, QuestionSerializer, OptionSerializer, Question, Option
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import QuestionSerializer
from customauth.permissions import AgentOnly
from agent.models import Agent
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from pscrestbackend.paginators.default_paginator import TenPerPagination

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


# list of question
class QuestionListView(BaseQuestionView, ListAPIView):
    """ question list view """
    serializer_class = QuestionResponseSerializer
    pagination_class = TenPerPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields =['created']
    search_fields=['text']
    filterset_fields =['text']


    def get_queryset(self):
        return Question.objects.filter(created_by__user=self.request.user)


# update question
class QuestionUpdateView(BaseQuestionView, UpdateAPIView):
    """ view for updating question with options """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


# get question
class QuestionDetailView(BaseQuestionView, RetrieveAPIView):
    """ question detail view """
    serializer_class = QuestionResponseSerializer
    queryset = Question.objects.all()


# delete question
class QuestionDeleteView(BaseQuestionView, DestroyAPIView):
    """ question delete view """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
