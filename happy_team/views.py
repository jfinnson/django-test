import datetime
from collections import defaultdict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.base import TemplateView, RedirectView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from happy_team.mixins import HappinessSubmissionRequiredMixin, NoHappinessSubmissionRequiredMixin
from happy_team.serializers import HappyHistorySerializer
from happy_team.models import HappyHistory, Team


class HappyRedirect(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # Get user's happiness submission today
        user_happiness_today = HappyHistory.objects.filter(user=self.request.user,
                                                           created_at__gte=datetime.date.today())

        # Redirect to stats if user has submitted happiness today, otherwise redirect to happiness submission form.
        if user_happiness_today:
            return reverse('happy-history-stats')
        else:
            return reverse('happy-history-add')


class HappyHistoryAdd(LoginRequiredMixin, NoHappinessSubmissionRequiredMixin, APIView):
    """
    View for rendering form to request user's happiness, and a post to allow it's submission.
    Redirects via mixin to stats if the user has already submitted today or after they are done submitting.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'happy_history/happy_history_add.html'

    @staticmethod
    def get(_):
        """ Render custom form template requesting user's happiness. Redirect if already submitted today via mixin. """
        return Response()

    def post(self, request):
        """ Save new entry into happiness history table, then redirect to stats. """

        # Request is passed to serializer so current user can be used in validation
        serializer = HappyHistorySerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(user=self.request.user)  # Manually set the user to the current session's user.
        return redirect('happy-history-stats')


class HappyHistoryStats(LoginRequiredMixin, HappinessSubmissionRequiredMixin, TemplateView):
    """
    View for rendering stats about the team's happiness.
    Redirects via mixin if user has not yet submitted happiness today.
    """
    template_name = "happy_history/happy_history_stats.html"

    def get_context_data(self, **kwargs):
        """ Collect stats on team happiness and include them in the template context """
        happy_history_by_level = defaultdict(int)
        total_happiness = 0
        number_of_users = 0
        user_ids = set()

        # Get teams that user belongs to
        teams = Team.objects.filter(teammember__user=self.request.user)
        team_ids = [team.id for team in teams]

        # Iterate through team(s) happiness history today and collect stats
        for entry in HappyHistory.objects.filter(created_at__gte=datetime.date.today(),
                                                 user__teammember__team_id__in=team_ids):
            # This query will 1 entry per team. I would use distinct but its not supposed by sqlite.
            if entry.user_id in user_ids:
                continue

            user_ids.add(entry.user_id)
            happy_history_by_level[entry.happy_level] += 1
            total_happiness += entry.happy_level
            number_of_users += 1

        # Add stats to template context
        context = super().get_context_data(**kwargs)
        context['teams'] = teams
        context['happy_history_by_level'] = happy_history_by_level
        context['happy_history_by_level_average'] = round(total_happiness/number_of_users, 2) if number_of_users else 0
        return context
