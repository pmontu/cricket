from django.db import models


class Team(models.Model):
	name = models.CharField(max_length=50, unique = True)
	color = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Player(models.Model):
	name = models.CharField(max_length=200)
	team = models.ForeignKey(Team)

	def __unicode__(self):
		return self.name

class Score(models.Model):
	score = models.PositiveIntegerField()
	date = models.DateField()
	player = models.ForeignKey(Player)