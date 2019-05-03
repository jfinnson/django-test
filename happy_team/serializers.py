from django.contrib.auth.models import User, Group
from rest_framework import serializers
from happy_team.models import HappyHistory


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class HappyHistorySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = HappyHistory
        fields = ('createdAt', 'happyLevel', 'user')
