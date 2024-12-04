# src/game/simulation.py

import random
from src.game.player_stats import Team

class Game:
    def __init__(self):
        self.team_a = Team('Kentucky')
        self.team_b = Team('Louisville')
        self.time_remaining = 40 * 60  # 48 minutes in seconds
        self.play_by_play = []

    def start_game(self):
        while self.time_remaining > 0:
            self.simulate_play()
            self.time_remaining -= random.randint(1, 30)  # Simulate time passing

    def simulate_play(self):
        scoring_team = random.choice([self.team_a, self.team_b])
        player = random.choice(scoring_team.players)
        points = random.choice([0, 2, 3])
        if points > 0:
            player.score_points(points)
            scoring_team.add_score(points)
            self.play_by_play.append(f"{player.name} of {scoring_team.name} scored {points} points")
        else:
            player.miss_shot()
            self.play_by_play.append(f"{player.name} of {scoring_team.name} missed a shot")

    def display_score(self):
        print(f"{self.team_a.name}: {self.team_a.score} - {self.team_b.name}: {self.team_b.score}")

    def display_play_by_play(self):
        for play in self.play_by_play:
            print(play)

    def display_box_score(self):
        print(f"Box Score for {self.team_a.name}")
        for player in self.team_a.players:
            print(player.get_stats())
        print(f"Box Score for {self.team_b.name}")
        for player in self.team_b.players:
            print(player.get_stats())

# Example usage
if __name__ == "__main__":
    game = Game()
    game.start_game()
    game.display_score()
    game.display_play_by_play()
    game.display_box_score()
