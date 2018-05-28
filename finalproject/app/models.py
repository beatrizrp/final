from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

import random 


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
    numberRounds = models.IntegerField('Nº Rondas', default = 2, validators=[MinValueValidator(1)])
    strengthWeigth = models.IntegerField('Peso Fuerza', default = 0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    dexterityWeigth = models.IntegerField('Peso Destreza', default = 0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    resistanceWeigth = models.IntegerField('Peso Resistencia', default = 0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    fighters = models.ManyToManyField(Fighter, verbose_name='Luchadores')
    classified1 = models.ForeignKey(Fighter, verbose_name = '1º clasificado', blank = True, null=True, related_name='tournamentClassified1', on_delete= models.CASCADE)
    classified2 = models.ForeignKey(Fighter, verbose_name = '2º clasificado', blank = True, null=True, related_name='tournamentClassified2', on_delete= models.CASCADE)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Torneo'


    def combat(L1, L2):
        rL1 = 0
        rL2 = 0

        while ((rL1<2) or (rL2 < 2)):
            pL1 = random.randint(0, L1.strength) * Tournament.strengthWeigth + random.randint(0, L1.dexterity) * Tournament.dexterityWeigth + random.randint(0, L1.resistance) * Tournament.resistanceWeigth
            pL2 = random.randint(0, L2.strength) * Tournament.strengthWeigth + random.randint(0, L2.dexterity) * Tournament.dexterityWeigth + random.randint(0, L2.resistance) * Tournament.resistanceWeigth

            print(pL1)
            print(pL2)

            if (pL1 > pL2):
                rL1 += 1
                print('Luchador 1 gana la ronda')
                if (rL1 == 2):
                    print('Luchador 1 gana el combate')
                    return L1
            else:
                if (pL2 > pL1):
                   rL2 += 1
                   print('Luchador 2 gana la ronda')
                   if (rL2 == 2):
                    print('Luchador 2 gana el combate')
                    return L2


    def celebrateTournament(t_id):
        print('Empezamos')
        DF = dict()
        r = 1
        t = Tournament(t_id)
        f = t.fighters.all()
        dup={r:list(f)}
        DF.update(dup)
          
        while r <= t.numberRounds:
            l = 1
            dp={r+1:list()}
            DF.update(dp)
            while l <= len(DF[r]):
                lg = []
                lg += [t.combat(l, l +1) for l in DF[r][:len(DF[r]):2]]
            r += 1
        return DF




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



