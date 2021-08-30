from agent.models import Agent
from rest_framework_simplejwt.authentication import JWTAuthentication
from course.models import Course
from pscrestbackend.paginators.default_paginator import TenPerPagination
from student.models import Student
from student.serializers import StudentListResponseSerializer, StudentSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from customauth.permissions import AgentOnly
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework import status
from customauth.models import MyUser
# Create your views here.

# create or register student
# only agent can create or register student


@api_view(['POST'])
@permission_classes([IsAuthenticated, AgentOnly])
@authentication_classes([JWTAuthentication])
def register_student(request):
    """ registering student """
    if request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            email = data['email']
            if MyUser.objects.filter(email=email).count() > 0:
                return Response({"detail": "Already user exist with this email"}, status=status.HTTP_400_BAD_REQUEST)
            password = data['password']
            if len(password) < 6:
                return Response({"detail": "Password should be greater than 6"}, status=status.HTTP_400_BAD_REQUEST)
            user = MyUser.objects.create_user(
                email=email, password=password, role="STUDENT")
            serializer.save(owner=user, added_by=request.user,
                            created=timezone.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseStudentGenericClass():
    permission_classes = [IsAuthenticated, AgentOnly]
    authentication_classes = [JWTAuthentication]


# """ get students of particular agent"""
class GetStudentsOfAgent( ListAPIView):
    """ return all student of particular user"""
    serializer_class = StudentListResponseSerializer
    model = Student
    pagination_class = TenPerPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    ordering_fields =['name','created']
    search_fields =["name"]
    filterset_fields =['name']

    def get_queryset(self):
        # return Student.objects.filter(added_by=self.request.user)
        return Student.objects.all()

# student details


class StudentDetailView(BaseStudentGenericClass, RetrieveAPIView):
    """ detail api view """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# update student
class UpdateStudentView(BaseStudentGenericClass, UpdateAPIView):
    """ view for updating student """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# delete student
class DeleteStudentView(BaseStudentGenericClass, DestroyAPIView):
    """ delete student generic view """
    queryset = Student.objects.all()


# add course to student

# block student
