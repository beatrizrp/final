from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

TYPES = (
    (0, 'Fuerza'),
    (1, 'Destreza'),
    (2, 'Resistencia')
)


class Fighter(models.Model):
    userId = models.ForeignKey(User, verbose_name='Id Usuario', on_delete= models.CASCADE)
    alias = models.CharField('Alias', max_length = 20)
    strength = models.IntegerField('Fuerza', default= 0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    dexterity = models.IntegerField('Destreza', default= 0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    resistance = models.IntegerField('Resistencia', default= 0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return self.alias
    
    class Meta:
        verbose_name = 'Luchador'
        verbose_name_plural = 'Luchadores'

class Tournament(models.Model):
    name = models.CharField('Nombre', max_length = 25)
    create_date = models.DateField('Fecha de Creación')
    start_date = models.DateField('Fecha de Inicio')
    numberPlayers = models.IntegerField('Nº Jugadores', default = 0)
    type = models.IntegerField('Tipo', default= 0, choices= TYPES)
    strengthWeigth = models.IntegerField('Peso Fuerza', default = 0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    dexterityWeigth = models.IntegerField('Peso Destreza', default = 0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    resistanceWeigth = models.IntegerField('Peso Resistencia', default = 0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    classified1 = models.ForeignKey(Fighter, verbose_name = '1º clasificado',related_name='tournamentClassified1', on_delete= models.CASCADE)
    classified2 = models.ForeignKey(Fighter, verbose_name = '2º clasificado',related_name='tournamentClassified2', on_delete= models.CASCADE)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Torneo'



class Combat(models.Model):
    tournament = models.ForeignKey(Tournament, verbose_name = 'Torneo', on_delete = models.CASCADE)
    alias1 = models.ForeignKey(Fighter, verbose_name='Luchador 1', related_name= 'combatAlias1', on_delete= models.CASCADE)
    alias2 = models.ForeignKey(Fighter, verbose_name='Luchador 2', related_name= 'combatAlias2', on_delete= models.CASCADE)
    timeStep = models.DateTimeField('Fecha')
    points1 = models.IntegerField('Puntos 1', default = 0)
    points2 = models.IntegerField('Puntos 2', default = 0)
    winner = models.ForeignKey(Fighter, verbose_name='Ganador', related_name= 'combat_winner', on_delete= models.CASCADE)
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Combate'



