from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.ExamCreateView.as_view(), name='exam_create'),
    path('all/', views.ExamListView.as_view(), name='exam_list'),
    path('detail/<int:pk>', views.ExamDetailView.as_view(), name='exam_detail'),
    path('update/<int:pk>', views.ExamUpdateView.as_view(), name='exam_update'),
    path('delete/<int:pk>', views.ExamDeleteView.as_view(), name='exam_delete'),

]