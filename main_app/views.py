from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Player, Teammate
from .forms import MatchStatsForm

# Create your views here.
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def players_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', {
        'players': players
    })

def players_detail(request, player_id):
    player = Player.objects.get(id = player_id)
    id_list = player.teammates.all().values_list('id')
    teammates_player_doesnt_have = Teammate.objects.exclude(id__in=id_list)
    matchstats_form = MatchStatsForm()
    return render(request, 'players/detail.html', {
        'player': player, 'matchstats_form': matchstats_form,
        'teammates': teammates_player_doesnt_have
    })

def add_matchstats(request, player_id):
    # create a ModelForm instance using the data in request.POST
    form = MatchStatsForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_matchstats = form.save(commit=False)
        new_matchstats.player_id = player_id
        new_matchstats.save()
    return redirect('detail', player_id=player_id)

class PlayerCreate(CreateView):
    model = Player
    fields = ['name', 'age', 'team', 'description']

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['age', 'team', 'description']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players'

class TeammateList(ListView):
  model = Teammate

class TeammateDetail(DetailView):
  model = Teammate

class TeammateCreate(CreateView):
  model = Teammate
  fields = '__all__'

class TeammateDelete(DeleteView):
  model = Teammate
  success_url = '/teammates'

def assoc_teammate(request, player_id, teammate_id):
  Player.objects.get(id=player_id).teammates.add(teammate_id)
  return redirect('detail', player_id=player_id)

def unassoc_teammate(request, player_id, teammate_id):
  Player.objects.get(id=player_id).teammates.remove(teammate_id)
  return redirect('detail', player_id=player_id)