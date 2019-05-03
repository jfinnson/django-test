from django.urls import path
from happy_team import views

urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('happy_history/', views.HappyHistoryList.as_view(), name='happy-history-list'),
]
