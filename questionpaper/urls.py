from django.urls import path
from .views import (
    QuestionPaperDeleteView, QuestionPaperListView,QuestionPaperCreateView,AddQuestionToQuestionPaper,QuestionPapersView,
    QuestionPaperQuestionDeleteView
)

urlpatterns = [
    path("all", QuestionPaperListView.as_view(), name='question_paper_list'),
    path("add/", QuestionPaperCreateView.as_view(), name='question_paper_create'),
    path("delete/<int:pk>", QuestionPaperDeleteView.as_view(), name='question_paper_create'),
    path("add/question", AddQuestionToQuestionPaper.as_view(), name='add_question_to_question_paper'),
    path("paper/all", QuestionPapersView.as_view(), name='question_papers'),
    path("paper/delete/<int:pk>", QuestionPaperQuestionDeleteView.as_view(), name='question_paper_delete'),
]