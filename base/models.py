from django.db import models

class BattleLog(models.Model):
	winner = models.IntegerField()
	gesture = models.CharField(max_length=20)