from django.urls import path
from course.views import AddUsersToCourse, CourseCreateView, CourseDeleteView, CourseDetailView, CourseListView, CourseUpdateView, RemoveStudentCourseView
urlpatterns = [
    path('add/', CourseCreateView.as_view(), name='create_course'),
    path('all/', CourseListView.as_view(), name='get_courses'),
    path('detail/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('update/<int:pk>', CourseUpdateView.as_view(), name='course_update'),
    path('delete/<int:pk>', CourseDeleteView.as_view(), name='course_delete'),
    # add or remove courses
    path('student/add/<int:pk>', AddUsersToCourse.as_view(), name='add-student-course'),
    path('student/remove/<int:pk>', RemoveStudentCourseView.as_view(), name='add-student-course'),
]