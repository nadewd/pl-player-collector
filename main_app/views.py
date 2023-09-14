from django.shortcuts import render

# Create your views here.
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def players_index(request):
    # We pass data to a template the same way we did in Express
    return render(request, 'players/index.html', {
        'players': players
    })

