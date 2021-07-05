from django.urls import path
from .views import register_agent, AgentListView

urlpatterns = [
    path('register', register_agent, name='register_agent'),
    path('', AgentListView.as_view(), name='agent'),
]
