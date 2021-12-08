from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.


class Game(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    api_game_id = models.TextField()
    away_team = models.CharField(max_length=50)
    home_team = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    winner = models.CharField(max_length=1)
