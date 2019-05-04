from django.contrib import admin
from happy_team.models import HappyHistory, Team, TeamMember

admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(HappyHistory)
