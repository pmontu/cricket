from django.shortcuts import render
from analysis.models import *

def home(request):
	players = Player.objects.all()
	return render(request, 'analysis/players.html', {"players":players})


