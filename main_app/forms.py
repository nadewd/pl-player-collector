from django.forms import ModelForm
from .models import MatchStats

class MatchStatsForm(ModelForm):
  class Meta:
    model = MatchStats
    fields = ['date', 'opponent', 'minutes', 'goals', 'assists', 'yellow_cards', 'red_card']