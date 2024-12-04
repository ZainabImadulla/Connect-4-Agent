import customtkinter
import tkinter as tk
from board import Board

from minimax_v_minimax import TwoMinimax
from minimax_game import SingleMinimax
from game import TwoPlayer
from minimax_v_random import MinimaxVRandom
from MainMenu import MainMenu

class Connect4(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Connect Four")
        self.geometry("700x650")
        
        self.MainMenu = MainMenu(self)
        self.TwoMinimax = TwoMinimax(self)
        self.PlayerVMinimax = SingleMinimax(self)
        self.TwoPlayer = TwoPlayer(self)
        self.MinimaxVRandom = MinimaxVRandom(self)

        self.MainMenu.pack(fill="both", expand=True)

    def switch_frame(self, frame_class):

        for frame in self.winfo_children():
            frame.pack_forget()

        if frame_class == "MainMenu":
            self.MainMenu = MainMenu(self)
            self.MainMenu.pack(fill="both", expand=True)
        elif frame_class == "TwoMinimax":
            self.TwoMinimax = TwoMinimax(self)
            self.TwoMinimax.pack(fill="both", expand=True)
        elif frame_class == "SingleMinimax":
            self.PlayerVMinimax = SingleMinimax(self)
            self.PlayerVMinimax.pack(fill="both", expand=True)
        elif frame_class == "TwoPlayer":
            self.TwoPlayer = TwoPlayer(self)
            self.TwoPlayer.pack(fill="both", expand=True)
        elif frame_class == "Random":
            self.MinimaxVRandom = MinimaxVRandom(self)
            self.MinimaxVRandom.pack(fill="both", expand=True)

def main():
    app = Connect4()
    app.mainloop()

if __name__ == "__main__":
    main()