from django.urls import path
from course.views import CourseCreateView, CourseDeleteView, CourseDetailView, CourseListView, CourseUpdateView
urlpatterns = [
    path('add/', CourseCreateView.as_view(), name='create_course'),
    path('list/', CourseListView.as_view(), name='get_courses'),
    path('detail/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('update/<int:pk>', CourseUpdateView.as_view(), name='course_update'),
    path('delete/<int:pk>', CourseDeleteView.as_view(), name='course_delete'),
]