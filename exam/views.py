from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from pscrestbackend.paginators.default_paginator import TenPerPagination


# Create your views here.
from agent.models import Agent
from exam.models import Exam
from exam.serializers import ExamDetailSerializer, ExamResponseSerializer, ExamSerializer
from customauth.permissions import AgentOnly


class BaseExamView:
    permission_classes = [IsAuthenticated, AgentOnly]
    authentication_classes = [JWTAuthentication]


class ExamCreateView(BaseExamView, CreateAPIView):
    """ api for create exam"""
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

    def perform_create(self, serializer):
        agent = Agent.objects.get(user__email=self.request.user)
        serializer.save(created_by=agent)


class ExamListView(BaseExamView, ListAPIView):
    serializer_class = ExamResponseSerializer
    pagination_class = TenPerPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    search_fields=['name']
    ordering_fields =['name']
    filterset_fields =['name']

    def get_queryset(self):
        return Exam.objects.filter(created_by__user = self.request.user)

class ExamDetailView( RetrieveAPIView):
    serializer_class = ExamDetailSerializer
    queryset = Exam.objects.all()


class ExamUpdateView(BaseExamView,UpdateAPIView):
    """ update exam """
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class ExamDeleteView(BaseExamView,DestroyAPIView):
    """ delete exam """
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
















