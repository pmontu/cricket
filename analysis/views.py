from django.shortcuts import render
from analysis.models import *
import json
from django.http import HttpResponse

def home(request):
	#players = Player.objects.all()
	#return render(request, 'analysis/players.html', {"players":players})
	return HttpResponse("Hello World")

def team_post(request):
	data = request.body
	d = json.loads(data)
	team = Team()
	team.name = d['name'] if 'name' in d else None 
	team.color = d['color'] if 'color' in d else None
	team.save()
	id = team.id
	return HttpResponse(id)

def teams(request):
	teams = Team.objects.all()
	list = []
	for team in teams:
		dict = {}
		dict['name'] = team.name
		dict['color'] = team.color
		dict['id'] = team.id
		list.append(dict)

	return HttpResponse(json.dumps(list))

def delete_team(request):
	data = request.body
	team = Team.objects.get(id=int(data)).delete()
	return HttpResponse(team)