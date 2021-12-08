from django.urls import path
from . import views

urlpatterns = [
    path('bets/', views.BetList.as_view()),
]
