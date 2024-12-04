import pygame
import tkinter as tk
from game.game_engine import GameEngine
from ui.interface import Interface

def main():
    # Initialize game engine
    game_engine = GameEngine()
    
    # Initialize user interface
    root = tk.Tk()
    app = Interface(root, game_engine)
    
    # Start the game
    root.mainloop()

if __name__ == "__main__":
    main()
