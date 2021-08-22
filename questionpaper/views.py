from rest_framework import serializers
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from customauth.permissions import AgentOnly
from pscrestbackend.paginators.default_paginator import TenPerPagination
from rest_framework.authentication import TokenAuthentication
# Create your views here.

from questionpaper.models import QuestionPaper, QuestionPaperQuestion
from questionpaper.serializers import QuestionPaperQuestionResponseSerializer, QuestionPaperQuestionSerializer, QuestionPaperResponseSerializer, QuestionPaperSerializer
from agent.models import Agent


class BaseQuestionPaperView():
    permission_classes = [IsAuthenticated, AgentOnly]
    authentication_classes = [TokenAuthentication]


class QuestionPaperListView(BaseQuestionPaperView, ListAPIView):
    model = QuestionPaper
    serializer_class = QuestionPaperResponseSerializer
    queryset = QuestionPaper.objects.all()
    pagination_class=TenPerPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    ordering_fields = ['title']
    search_fields =['title']
    filterset_fields = ['title']


class QuestionPaperCreateView(BaseQuestionPaperView,CreateAPIView):
    model = QuestionPaper
    serializer_class = QuestionPaperSerializer
    queryset = QuestionPaper.objects.all()
    def perform_create(self, serializer):
        agent = Agent.objects.get(user=self.request.user)
        serializer.save(added_by=agent)

class AddQuestionToQuestionPaper(BaseQuestionPaperView,CreateAPIView):
    """ add question to question paper"""
    serializer_class = QuestionPaperQuestionSerializer
    model = QuestionPaperQuestion
    queryset= QuestionPaperQuestion.objects.all()


class QuestionPaperDeleteView(BaseQuestionPaperView,DestroyAPIView):
    model = QuestionPaper
    queryset= QuestionPaper.objects.all()



# many to many relational object 
class QuestionPapersView(BaseQuestionPaperView,ListAPIView):
    serializer_class = QuestionPaperQuestionResponseSerializer
    model = QuestionPaperQuestion
    queryset= QuestionPaperQuestion.objects.all()



class QuestionPaperQuestionDeleteView(BaseQuestionPaperView,DestroyAPIView):
    model = QuestionPaperQuestion
    queryset= QuestionPaperQuestion.objects.all()









