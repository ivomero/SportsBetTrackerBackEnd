from rest_framework import serializers
from .models import Games

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['id', 'user_id', 'comment_id', 'away_team', 'home_team', 'start_time', 'winner']