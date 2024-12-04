import customtkinter
import tkinter as tk
from board import Board


class MainMenu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
    
        self.label = customtkinter.CTkLabel(self, text="Choose a Game Mode")
        self.label.pack(side='top')
        self.buttonTwoPlayer = customtkinter.CTkButton(self, 200, 100, text="Player vs Player", fg_color="#2a2b2e", bg_color="#2a2b2e", command = lambda: self.runTwoPlayer())
        self.buttonTwoPlayer.pack(side='top', padx=6, pady=(50, 4))
        self.buttonPlayerVMinimax = customtkinter.CTkButton(self, 200, 100, text="Player vs Minimax",  fg_color="#2a2b2e", bg_color="#2a2b2e", command = lambda: self.runPlayerVMinimax())
        self.buttonPlayerVMinimax.pack(side='top', padx=6, pady=4)
        self.buttonTwoMinimax = customtkinter.CTkButton(self, 200, 100, text="Minimax vs Minimax",  fg_color="#2a2b2e", bg_color="#2a2b2e", command = lambda: self.runTwoMinimax())
        self.buttonTwoMinimax.pack(side='top', padx=6, pady=4)
        self.buttonMinimaxVRandom = customtkinter.CTkButton(self, 200, 100, text="Minimax vs Random",  fg_color="#2a2b2e", bg_color="#2a2b2e", command = lambda: self.runMinimaxVRandom())
        self.buttonMinimaxVRandom.pack(side='top', padx=6, pady=4)

    def runTwoPlayer(self):
        self.master.switch_frame("TwoPlayer")
    def runPlayerVMinimax(self):
        self.master.switch_frame("SingleMinimax")
    def runTwoMinimax(self):
        self.master.switch_frame("TwoMinimax")
    def runMinimaxVRandom(self):
        self.master.switch_frame("Random")


