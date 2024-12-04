# src/game/game_engine.py

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.assists = 0
        self.rebounds = 0

    def score_points(self, points):
        self.points += points

    def record_assist(self):
        self.assists += 1

    def record_rebound(self):
        self.rebounds += 1

class Team:
    def __init__(self, name):
        self.name = name
        self.players = [Player(f"Player {i+1}") for i in range(5)]
        self.score = 0

    def add_score(self, points):
        self.score += points

class Game:
    def __init__(self):
        self.team_a = Team('Kentucky')
        self.team_b = Team('Louisville')
        self.time_remaining = 48 * 60  # 48 minutes in seconds
        self.play_by_play = []

    def start_game(self):
        while self.time_remaining > 0:
            self.simulate_play()
            self.time_remaining -= random.randint(1, 24)  # Simulate time passing

    def simulate_play(self):
        scoring_team = random.choice([self.team_a, self.team_b])
        player = random.choice(scoring_team.players)
        points = random.choice([2, 3])
        player.score_points(points)
        scoring_team.add_score(points)
        self.play_by_play.append(f"{player.name} of {scoring_team.name} scored {points} points")

    def display_score(self):
        print(f"{self.team_a.name}: {self.team_a.score} - {self.team_b.name}: {self.team_b.score}")

    def display_play_by_play(self):
        for play in self.play_by_play:
            print(play)

# Example usage
if __name__ == "__main__":
    game = Game()
    game.start_game()
    game.display_score()
    game.display_play_by_play()
