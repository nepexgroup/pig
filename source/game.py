# Pig = None
import random


class Pig:
    def __init__(self, *players):
        self.players = players
        self.scores = dict.fromkeys(self.players, 0)

    def get_players(self):
        """Return a tuple of all players"""
        return self.players

    def roll(self):
        """Return a number between 1 and 6"""
        return random.randint(1, 6)

    def get_score(self):
        return self.scores
