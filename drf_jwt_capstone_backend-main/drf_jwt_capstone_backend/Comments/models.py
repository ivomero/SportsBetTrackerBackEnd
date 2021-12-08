from Games.models import Game
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
User = get_user_model()

# Create your models here.


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    game_id = models.ForeignKey(Game, on_delete=CASCADE)
