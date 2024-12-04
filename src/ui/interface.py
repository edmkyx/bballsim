
# src/ui/interface.py

import tkinter as tk
from tkinter import ttk

class Interface:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.root.title("Basketball Simulation")
        
        # Main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Play-by-play text area
        self.play_by_play_label = ttk.Label(self.main_frame, text="Play-by-Play Commentary")
        self.play_by_play_label.grid(row=0, column=0, sticky=tk.W)
        self.play_by_play_text = tk.Text(self.main_frame, width=50, height=20)
        self.play_by_play_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Box score text area
        self.box_score_label = ttk.Label(self.main_frame, text="Box Score")
        self.box_score_label.grid(row=0, column=1, sticky=tk.W)
        self.box_score_text = tk.Text(self.main_frame, width=50, height=20)
        self.box_score_text.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Display initial game state
        self.update_play_by_play()
        self.update_box_score()
    
    def update_play_by_play(self):
        self.play_by_play_text.delete(1.0, tk.END)
        for play in self.game.play_by_play:
            self.play_by_play_text.insert(tk.END, play + "\n")
    
    def update_box_score(self):
        self.box_score_text.delete(1.0, tk.END)
        self.box_score_text.insert(tk.END, f"Box Score for {self.game.team_a.name}\n")
        for player in self.game.team_a.players:
            self.box_score_text.insert(tk.END, str(player.get_stats()) + "\n")
        self.box_score_text.insert(tk.END, f"\nBox Score for {self.game.team_b.name}\n")
        for player in self.game.team_b.players:
            self.box_score_text.insert(tk.END, str(player.get_stats()) + "\n")

# Example usage
if __name__ == "__main__":
    from src.game.simulation import Game
    
    root = tk.Tk()
    game = Game()
    game.start_game()
    app = Interface(root, game)
    root.mainloop()
