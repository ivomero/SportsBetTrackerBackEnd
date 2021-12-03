from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentsList.as_view()),
]
