import customtkinter
import tkinter as tk
from board import Board


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.player = 1
        self.board = Board()
        self.buttons = [[0] * 7 for i in range(6)]
        self.label = customtkinter.CTkLabel(self, text="Player 1's Turn")
        self.label.grid(row=0, column=3)
        # add widgets onto the frame, for example:
        self.transparent = tk.PhotoImage(file="./empty.png")
        self.player1 = tk.PhotoImage(file="./player1.png")
        self.player2 = tk.PhotoImage(file="./player2.png")
        for i in range(6):
            for j in range(7):
                self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.transparent, fg_color="#2a2b2e", bg_color="#2a2b2e", command= lambda j=j: self.handle_click(j))
                self.buttons[i][j].grid(row=i+1, column=j)

    def handle_click(self, column):
        if(self.board.move_possible(column)):
            self.board.add_coin(column, self.player)
            self.update_board()
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
                    self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.player1, fg_color="#2a2b2e", bg_color="#2a2b2e", command=lambda j=j:self.handle_click(j), state="disabled")
                    self.buttons[i][j].grid(row=i+1, column=j)
                elif(current_board[i][j] == 2):
                    self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.player2, fg_color="#2a2b2e", bg_color="#2a2b2e", command=lambda j=j:self.handle_click(j), state="disabled")
                    self.buttons[i][j].grid(row=i+1, column=j)
                else:
                    self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.transparent, fg_color="#2a2b2e", bg_color="#2a2b2e", command=lambda j=j:self.handle_click(j), state="disabled")
                    self.buttons[i][j].grid(row=i+1, column=j)


    def update_board(self):
        current_board = self.board.getBoard()
        for i in range(6):
            for j in range(7):
                if(current_board[i][j] == 1):
                    self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.player1, fg_color="#2a2b2e", bg_color="#2a2b2e", command=lambda j=j:self.handle_click(j))
                    self.buttons[i][j].grid(row=i+1, column=j)
                elif(current_board[i][j] == 2):
                    self.buttons[i][j] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.player2, fg_color="#2a2b2e", bg_color="#2a2b2e", command=lambda j=j:self.handle_click(j))
                    self.buttons[i][j].grid(row=i+1, column=j)



def main():
    app = App()
    app.mainloop()  

if __name__ == "__main__":
    main()


