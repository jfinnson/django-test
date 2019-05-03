from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from happy_team.serializers import UserSerializer, TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = TeamSerializer
