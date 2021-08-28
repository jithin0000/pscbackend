from agent.models import Agent
from customauth.models import MyUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import AgentSerializer
from customauth.permissions import AdminOnly
# Create your views here.

# need to udpate it's permission, it's only accessabile for admins


@api_view(['POST'])
def register_agent(request):
    """ method for registering agent"""
    if request.method == "POST":
        data = request.data
        serializer = AgentSerializer(data=data)
        if serializer.is_valid():
            email = data['email']
            if MyUser.objects.filter(email=email).count() > 0:
                return Response({"detail": "Already user exist with this email"}, status=status.HTTP_400_BAD_REQUEST)
            password = data['password']
            if len(password) < 6:
                return Response({"detail": "Password should be greater than 6"}, status=status.HTTP_400_BAD_REQUEST)
            user = MyUser.objects.create_user(
                email=email, password=password, role="AGENT")
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgentListView(generics.ListAPIView, generics.GenericAPIView):
    """agent list api view"""

    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, AdminOnly, )
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
