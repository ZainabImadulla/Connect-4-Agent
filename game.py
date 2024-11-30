import customtkinter
import tkinter as tk
from board import Board

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.player = 1
        self.board = Board()
        self.buttons = [[0] * 7 for i in range(6)]
        # add widgets onto the frame, for example:
        self.transparent = tk.PhotoImage(file="./empty.png")
        self.player1 = tk.PhotoImage(file="./player1.png")
        self.player2 = tk.PhotoImage(file="./player2.png")
        for x in range(6):
            for y in range(7):
                self.buttons[x][y] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.transparent, fg_color="#2a2b2e", bg_color="#2a2b2e", command= lambda y=y: self.handle_click(y))
                self.buttons[x][y].grid(row=x, column=y)

    def handle_click(self, column):
        print(self.board.move_possible(column))
        if(self.board.move_possible(column)):
            self.board.add_coin(column, self.player)
            if(self.player == 1):
                self.player = 2
            else:
                self.player = 1
            self.update_board()
        

    def update_board(self):
        current_board = self.board.getBoard()
        print()
        for x in range(6):
            for y in range(7):
                if(current_board[x][y] == 1):
                    self.buttons[x][y] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.player1, fg_color="#2a2b2e", bg_color="#2a2b2e", command=lambda y=y:self.handle_click(y))
                    self.buttons[x][y].grid(row=x, column=y)
                elif(current_board[x][y] == 2):
                    self.buttons[x][y] = customtkinter.CTkButton(self, 100, 87.5, text="", image=self.player2, fg_color="#2a2b2e", bg_color="#2a2b2e", command=lambda y=y:self.handle_click(y))
                    self.buttons[x][y].grid(row=x, column=y)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x700")
        self.label = customtkinter.CTkLabel(self, text="Player 1's Turn")

        self.label.pack(padx=20, pady=20)

        self.my_frame = MyFrame(master=self)
        self.my_frame.pack(padx=20, pady=20)


def main():
    app = App()
    app.mainloop()  

if __name__ == "__main__":
    main()


