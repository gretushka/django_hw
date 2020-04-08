from django.db import models


class Player(models.Model):
    def __str__(self):
        return self.id



class Game(models.Model):
    players = models.ManyToManyField(Player, related_name='games', through='PlayerGameInfo')
    min_value = models.IntegerField(default=1)
    max_value = models.IntegerField(default=1000)
    game_value = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.id


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)


    def __str__(self):
        return '{0}_{1}'.format(self.player, self.game)
