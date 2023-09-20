from django.contrib import admin
from .models import Player, MatchStats

# Register your models here.
admin.site.register(Player)
admin.site.register(MatchStats)