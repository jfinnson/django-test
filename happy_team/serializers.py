from rest_framework import serializers
from happy_team.models import HappyHistory


class HappyHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HappyHistory
        fields = ('created_at', 'happy_level', 'user')
        # Allow user to be set only in HappyHistoryList.perform_create
        extra_kwargs = {
            'user': {'read_only': True}
        }
