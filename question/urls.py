from django.urls import path
from . views import QuestionCreateView, QuestionUpdateView

urlpatterns = [
    path('add/', QuestionCreateView.as_view(), name='create_question'),
    path('update/<int:pk>/', QuestionUpdateView.as_view(), name='update_question'),
]
