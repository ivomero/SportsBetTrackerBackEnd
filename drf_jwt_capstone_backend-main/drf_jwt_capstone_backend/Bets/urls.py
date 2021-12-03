from django.urls import path
from . import views

urlpatterns = [
    path('bets/', views.BetsList.as_view()),
]
