# main.py

import tkinter as tk
from src.game.simulation import Game
from src.ui.interface import Interface

def main():
    # Initialize game engine
    game = Game()
    game.start_game()
    
    # Initialize user interface
    root = tk.Tk()
    app = Interface(root, game)
    
    # Start the game
    root.mainloop()

if __name__ == "__main__":
    main()
