from django.urls import path
from . import views

urlpatterns = [
    path("details", views.GetUserDetails.as_view(), name="user_detail")
]
