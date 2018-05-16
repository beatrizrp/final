from django.contrib import admin
import site
from .models import *


class FighterAdmin(admin.ModelAdmin):
    list_display = ['userId', 'alias', 'strength', 'dexterity', 'resistance']
    search_fields = ['alias']

class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_date', 'start_date', 'numberPlayers', 'type', 'strengthWeigth', 'dexterityWeigth', 'resistanceWeigth',
                    'classified1', 'classified2', 'classified3']
    search_fields = ['name', 'create_date', 'start_date', 'classified1', 'classified2', 'classified3']
    list_filter = ['start_date', 'create_date', 'start_date' ]

class CombatAdmin(admin.ModelAdmin):
    list_display = [ 'tournament', 'alias1', 'alias2', 'timeStep', 'points1', 'points2', 'winner']
    search_fields = ['winner']
    list_filter = ['tournament']

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Fighter, FighterAdmin)
admin.site.register(Combat, CombatAdmin)