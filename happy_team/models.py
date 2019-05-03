from django.db import models
from django.contrib.auth.models import User


class HappyHistory(models.Model):
    """
    Model that tracks the happiness of users for each day.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    happy_level = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'Happy history'
