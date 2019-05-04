import datetime

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

    def validate(self, data):
        """
        Custom validation:
        - Ensure the entry is unique for current date
        - Check that happy_level is between 1-5.
        """
        user_happiness_today = HappyHistory.objects.filter(user=self.context.get('request').user,
                                                           created_at__gte=datetime.date.today())
        if user_happiness_today:
            raise serializers.ValidationError("User already recorded happiness today")
        if not (1 <= data.get('happy_level') <= 5):
            raise serializers.ValidationError("happy_level must be between 1-5")
        return data
