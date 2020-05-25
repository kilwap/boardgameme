from django.db import models

class Game(models.Model):
	game_id = models.DecimalField(max_digits=7, decimal_places=0)
	title = models.CharField(max_length=300, default=None)
	description = models.TextField(default="No description yet, sorry :)")
	min_players = models.DecimalField(max_digits=2, decimal_places=0, default=0)
	max_players = models.DecimalField(max_digits=2, decimal_places=0, default=0)
	age = models.DecimalField(max_digits=2, decimal_places=0, default=0)
	pub_year = models.DecimalField(max_digits=4, decimal_places=0, default=0)
	category = models.CharField(max_length=200, default="Unknown")
	publisher = models.CharField(max_length=100, default="Unknown")



