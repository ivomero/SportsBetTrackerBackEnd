from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.


class Games(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(
        'Comments.Comments', on_delete=models.CASCADE)
    away_team = models.CharField(max_length=50)
    home_team = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    winner = models.CharField(max_length=1)
