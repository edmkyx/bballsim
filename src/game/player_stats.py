# src/game/player_stats.py

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.assists = 0
        self.rebounds = 0
        self.field_goals_attempted = 0
        self.field_goals_made = 0

    def score_points(self, points):
        self.points += points
        self.field_goals_attempted += 1
        self.field_goals_made += 1

    def miss_shot(self):
        self.field_goals_attempted += 1

    def record_assist(self):
        self.assists += 1

    def record_rebound(self):
        self.rebounds += 1

    def get_stats(self):
        return {
            "points": self.points,
            "assists": self.assists,
            "rebounds": self.rebounds,
            "fg_attempted": self.field_goals_attempted,
            "fg_made": self.field_goals_made
        }

class Team:
    def __init__(self, name):
        self.name = name
        self.players = [Player(f"Player {i+1}") for i in range(5)]
        self.score = 0

    def add_score(self, points):
        self.score += points

    def get_team_stats(self):
        return {
            "team_score": self.score,
            "players": [player.get_stats() for player in self.players]
        }
