from pscrestbackend.paginators.default_paginator import TenPerPagination
from agent.models import Agent
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from customauth.permissions import AgentOnly
from rest_framework.authentication import TokenAuthentication
from . serializers import CourseSerializer, Course,CourseResponseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class BaseCourseClass():
    permission_classes = [IsAuthenticated,AgentOnly]
    authentication_classes =[TokenAuthentication]
 

# Create your views here.
class CourseCreateView(BaseCourseClass,CreateAPIView):
    """ create course """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    def perform_create(self,serializer):
        agent = Agent.objects.get(user=self.request.user)
        serializer.save(created_by = agent, status="CREATED")


class CourseListView(BaseCourseClass,ListAPIView):
    """ list of courses of particular agent """
    serializer_class = CourseResponseSerializer 
    pagination_class = TenPerPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields =['title']
    filterset_fields =['title']


    def get_queryset(self):
        return Course.objects.filter(created_by__user=self.request.user)

class CourseDetailView(BaseCourseClass,RetrieveAPIView):
    """ course detail view """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseUpdateView( BaseCourseClass,UpdateAPIView):
    """ update course view """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseDeleteView(BaseCourseClass, DestroyAPIView):
    """ course delete view"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


# TODO:// add or remove student to course