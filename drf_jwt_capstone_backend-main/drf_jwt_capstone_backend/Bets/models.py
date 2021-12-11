from django.db import models
from django.contrib.auth import get_user_model
from Games.models import Game
User = get_user_model()

# Create your models here.


class Bet(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    unit_bet = models.IntegerField(default=0)
    team = models.CharField(max_length=50)
    game_id = models.CharField(max_length=200)
