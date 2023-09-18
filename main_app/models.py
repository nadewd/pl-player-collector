from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

# Changing this instance method
# does not impact the database, therefore
# no makemigrations is necessary
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})

class MatchStats(models.Model):
    opponent = models.CharField(max_length=100)
    date = models.DateField()
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
        return f'v {self.get_opponent_display()} - {self.get_date_display()}'