from django.db import models
from django.contrib.auth.models import User


class HappyHistory(models.Model):
    """
    Model that tracks the happiness of users for each day.
    """
    createdAt = models.DateTimeField(auto_now_add=True)
    happyLevel = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique_for_date=createdAt)

    class Meta:
        ordering = ('createdAt',)
        verbose_name_plural = 'Happy history'

    def create(self, validated_data):
        """
        Create and return a new HappyHistory entry
        """
        return HappyHistory.objects.create(**validated_data)
