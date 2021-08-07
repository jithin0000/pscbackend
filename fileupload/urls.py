from django.urls import path
from .views import FileUploadView,ExtractTextFromImageView

urlpatterns = [
    path("file",FileUploadView.as_view(), name='file_upload'),
    path("extract",ExtractTextFromImageView.as_view(), name='extract_question_img')
]