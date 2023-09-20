from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator

# Create your models here.

class Teammate(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('teammates_detail', kwargs={'pk': self.id})

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    teammates = models.ManyToManyField(Teammate)

# Changing this instance method
# does not impact the database, therefore
# no makemigrations is necessary
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})

class MatchStats(models.Model):
    date = models.DateField('match date')
    opponent = models.CharField(max_length=100)
    minutes = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_card = models.IntegerField()

    # create a player_id FK
    player = models.ForeignKey(
        Player, 
        on_delete = models.CASCADE
        )
        
    def __str__(self):
        return f'{self.player} v {self.opponent} - {self.date}'

    class Meta:
        ordering = ['-date']

