from django.urls import path
from . views import QuestionCreateView, QuestionDeleteView, QuestionDetailView, QuestionListView, QuestionUpdateView

urlpatterns = [
    path('add/', QuestionCreateView.as_view(), name='create_question'),
    path('all/', QuestionListView.as_view(), name='list_question'),
    path('update/<int:pk>/', QuestionUpdateView.as_view(), name='update_question'),
    path('detail/<int:pk>/', QuestionDetailView.as_view(), name='detail_question'),
    path('delete/<int:pk>/', QuestionDeleteView.as_view(), name='delete_question'),
]
