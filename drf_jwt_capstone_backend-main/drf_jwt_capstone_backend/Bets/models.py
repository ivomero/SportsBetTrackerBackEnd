from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Bets(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    unit_bet = models.IntegerField()
    game_id = models.ForeignKey(
        'Games.Games', on_delete=models.CASCADE)
