from django.urls import path
from . views import register_student, GetStudentsOfAgent, DeleteStudentView, UpdateStudentView


urlpatterns = [
    path('register', register_student, name="register_student"),
    path('all', GetStudentsOfAgent.as_view(), name="get_students"),
    path('delete/<int:pk>', DeleteStudentView.as_view(), name="delete_student"),
    path('update/<int:pk>', UpdateStudentView.as_view(), name="update_student"),
]
