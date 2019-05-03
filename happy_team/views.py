from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from rest_framework import generics

from happy_team.serializers import HappyHistorySerializer, UserSerializer
from happy_team.models import HappyHistory


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class HomePage(TemplateView):
    template_name = 'home.html'


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HappyHistoryList(generics.ListCreateAPIView):
    queryset = HappyHistory.objects.all()
    serializer_class = HappyHistorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

