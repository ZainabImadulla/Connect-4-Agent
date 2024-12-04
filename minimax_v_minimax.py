import math
import customtkinter
import tkinter as tk
from board import Board



class TwoMinimax(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.player = 1
        self.board = Board()
        self.buttons = [[0] * 7 for i in range(6)]
        self.label = customtkinter.CTkLabel(self, text="Player 1's Turn")
        self.label.grid(row=0, column=3)
        self.back = customtkinter.CTkButton(self, 100, 87.5,fg_color="#a61111", bg_color="#2a2b2e",  text = "Back", command = lambda: self.menu())
        self.back.grid(row=0, column=6)

        self.reset = customtkinter.CTkButton(self, 100, 87.5,fg_color="#3d7d47", bg_color="#2a2b2e",  text = "Restart", command = lambda: self.resetBoard())
        self.reset.grid(row=0, column=5)

        self.transparent = tk.PhotoImage(file="./empty.png")
        self.player1 = tk.PhotoImage(file="./player1.png")
        self.player2 = tk.PhotoImage(file="./player2.png")
        self.start_button = customtkinter.CTkButton(self, 100, 87.5, text = "Begin Game!", command = lambda: self.handle_click())
        self.start_button.grid(row=0, column=0)
        for i in range(6):
            for j in range(7):
                self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.transparent, fg_color="#2a2b2e", bg_color="#2a2b2e")
                self.buttons[i][j].grid(row=i+1, column=j)

    def handle_click(self):
        self.start_button.grid_forget()
        while(not (self.board.check_won(1) or self.board.check_won(2) or self.board.is_board_full())):
            move, _ = self.board.minimax(4, -math.inf, math.inf, True, self.player, "offensive")
            self.board.add_coin(move, self.player)
            self.after(1000, self.update_board())
            self.label.grid_forget()
            if self.board.check_won(1):
                self.disable_board()
                self.label = customtkinter.CTkLabel(self, text="Player 1 Won")
            elif self.board.check_won(2):
                self.disable_board()
                self.label = customtkinter.CTkLabel(self, text="Player 2 Won")    
            elif self.board.is_board_full():
                self.disable_board()
                self.label = customtkinter.CTkLabel(self, text="Game Tied")  
            else:
                if(self.player == 1):
                    self.player = 2
                    self.label = customtkinter.CTkLabel(self, text="Player 2's Turn")
                else:
                    self.player = 1
                    self.label = customtkinter.CTkLabel(self, text="Player 1's Turn")
            self.label.grid(row=0, column=3)
        
    def disable_board(self):
        current_board = self.board.getBoard()
        for i in range(6):
            for j in range(7):
                if(current_board[i][j] == 1):
                    self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.player1, fg_color="#2a2b2e", bg_color="#2a2b2e", state="disabled")
                    self.buttons[i][j].grid(row=i+1, column=j)
                elif(current_board[i][j] == 2):
                    self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.player2, fg_color="#2a2b2e", bg_color="#2a2b2e",  state="disabled")
                    self.buttons[i][j].grid(row=i+1, column=j)
                else:
                    self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.transparent, fg_color="#2a2b2e", bg_color="#2a2b2e", state="disabled")
                    self.buttons[i][j].grid(row=i+1, column=j)


    def update_board(self):
        current_board = self.board.getBoard()
        for i in range(6):
            for j in range(7):
                if(current_board[i][j] == 1):
                    self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.player1, fg_color="#2a2b2e", bg_color="#2a2b2e")
                    self.buttons[i][j].grid(row=i+1, column=j)
                elif(current_board[i][j] == 2):
                    self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.player2, fg_color="#2a2b2e", bg_color="#2a2b2e")
                    self.buttons[i][j].grid(row=i+1, column=j)

    def menu(self):
            self.master.switch_frame("MainMenu")

    def resetBoard(self):
        self.master.switch_frame("TwoMinimax")

