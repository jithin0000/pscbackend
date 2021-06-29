from django.urls import path
from .views import register_agent

urlpatterns = [
    path('register', register_agent, name='register_agent')
]
