from django.db import models


class Leagues(models.Model):
    # league_id = models.IntegerField()
    name = models.CharField(max_length=50)
    rarity = models.CharField(max_length=50)


class Rewards(models.Model):
    gw = models.IntegerField()
    prize_pool = models.IntegerField()
    entrances = models.IntegerField()
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE)



