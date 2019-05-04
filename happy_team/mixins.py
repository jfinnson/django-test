import datetime

from django.shortcuts import redirect

from happy_team.models import HappyHistory


class HappinessSubmissionRequiredMixin:
    """
    Mixin to redirect to happiness submission page if user has not yet submitted today.
    """
    def dispatch(self, request, *args, **kwargs):
        # Get user's happiness submission today
        user_happiness_today = HappyHistory.objects.filter(user=request.user,
                                                           created_at__gte=datetime.date.today())

        # Redirect to happy-history-add if user has not submitted happiness today, otherwise continue to stats.
        if not user_happiness_today:
            return redirect('happy-history-add')
        else:
            return super().dispatch(request, *args, **kwargs)


class NoHappinessSubmissionRequiredMixin:
    """
    Mixin to redirect to happiness history stats page if user has already submitted happiness today.
    """
    def dispatch(self, request, *args, **kwargs):
        # Get user's happiness submission today
        user_happiness_today = HappyHistory.objects.filter(user=request.user,
                                                           created_at__gte=datetime.date.today())

        # Redirect to happy-history-add if user has not submitted happiness today, otherwise continue to stats.
        if user_happiness_today:
            return redirect('happy-history-stats')
        else:
            return super().dispatch(request, *args, **kwargs)
