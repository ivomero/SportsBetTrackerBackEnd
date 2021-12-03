from rest_framework import serializers
from .models import Bets


class BetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bets
        fields = ['id', 'user_id', 'unit_bet', 'game_id']
