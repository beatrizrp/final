from rest_framework import serializers
from .models import *

class FighterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fighter
        fields = ('id', 'userId', 'alias', 'strength', 'dexterity', 'resistance')

class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        fields = ('id', 'name', 'create_date', 'start_date', 'numberPlayers', 'type', 'strengthWeigth', 'dexterityWeigth', 
                  'resistanceWeigth', 'classified1', 'classified2', 'classified3')


class CombatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Combat
        fields = ('id', 'tournament', 'alias1', 'alias2', 'timeStep', 'points1', 'points2', 'winner')



