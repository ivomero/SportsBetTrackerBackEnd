from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'api_game_id', 'user_id',
                  'away_team', 'home_team', 'start_time', 'winner']
