from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    """
    Model representing each team
    """
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(User, through='TeamMember')

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    """
    Model that extends user and represents a member of a team
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


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
