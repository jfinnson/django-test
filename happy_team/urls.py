from django.urls import path
from happy_team import views

urlpatterns = [
    path('', views.HappyRedirect.as_view(), name='home'),
    path('happy_history/add/', views.HappyHistoryAdd.as_view(), name='happy-history-add'),
    path('happy_history/stats/', views.HappyHistoryStats.as_view(), name='happy-history-stats'),
]
