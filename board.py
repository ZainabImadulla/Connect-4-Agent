# Board.py
# Represents a board in a game of connect 4
class Board:
    def __init__(self, board=None):
        if(board == None):
            self.board = [[0] * 7 for i in range(6)]
        else:
            self.board = board


    def add_coin(self, column, player):
        for i in range(5, -1, -1):
            if not self.has_coin(i, column):
                self.board[i][column] = player
                break
        
    def move_possible(self, column):
        if column > 6 or column < 0:
            return False
        possible = False
        for i in range(5, -1, -1):
            possible = possible or not self.has_coin(i, column)
        
        return possible

    def has_coin(self, row, column):
        if self.board[row][column] == 0:
            return False
        return True
    
    def check_won(self):
        return self.check_vertical or self.check_horizontal or self.check_diagonal


    def check_vertical(self):
        for x in range(7):
            count = 0
            prev_coin = 0
            for y in range(6):
                if self.has_coin(y, x) and count == 0 and self.board[y][x] != prev_coin:
                    count = 1
                    prev_coin = self.board[y][x]
                elif self.has_coin(y, x) and prev_coin == self.board[y][x]:
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
                prev_coin = self.board[y][x]
        return False
                
    def check_horizontal(self):
        for x in range(6):
            count = 0
            prev_coin = 0
            for y in range(7):
                if self.has_coin(x, y) and count == 0 and self.board[x][y] != prev_coin:
                    count = 1
                    prev_coin = self.board[x][y]
                elif self.has_coin(x, y) and prev_coin == self.board[x][y]:
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
                prev_coin = self.board[x][y]
        return False

    def check_diagonal(self):
        for f in range(3, 6):
            count = 0
            x = 0
            prev_coin = 0
            for z in range(f, -1, -1):
                if self.has_coin(z, x) and count == 0 and self.board[z][x] != prev_coin:
                    count = 1
                    prev_coin = self.board[z][x]
                elif self.has_coin(z, x) and prev_coin == self.board[z][x]:
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
                prev_coin = self.board[z][x]
                x += 1
            if count >= 4:
                return True
        
        for f in range(1, 4):
            count = 0
            y = 5
            for z in range(f, 6):
                if self.has_coin(y, z) and count == 0 and self.board[y][z] != prev_coin:
                    count = 1
                    prev_coin = self.board[y][z]
                elif self.has_coin(y, z) and prev_coin == self.board[y][z]:
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
                prev_coin = self.board[y][z]
                y -= 1
            if count >= 4:
                return True


        for f in range(3, 6):
            count = 0
            x = 6
            prev_coin = 0
            for z in range(f, -1, -1):
                if self.has_coin(z, x) and count == 0 and self.board[z][x] != prev_coin:
                    count = 1
                    prev_coin = self.board[z][x]
                elif self.has_coin(z, x) and prev_coin == self.board[z][x]:
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
                prev_coin = self.board[z][x]
                x -= 1
            if count >= 4:
                return True

        for f in range(3, 7):
            count = 0
            y = 5
            prev_coin = 0
            for z in range(f, -1, -1):
                if self.has_coin(y, z) and count == 0 and self.board[y][z] != prev_coin:
                    count = 1
                    prev_coin = self.board[y][z]
                elif self.has_coin(y, z) and prev_coin == self.board[y][z]:
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
                prev_coin = self.board[y][z]
                y -= 1
            if count >= 4:
                return True
        
        return False
        
    def generate_next_states(self, player):
        next_states = []
        for i in range(7):
            new_board = Board(self.board)
            if self.move_possible(i):
                new_board.add_coin(i, player)
                next_states.append(new_board)
                #new_board.print_board()
                #print()
        return next_states
    
    def print_board(self):
        for i in range(6):
            for j in range(7):
                print(self.board[i][j],  end=" ")
            print()

    def getBoard(self):
        self.print_board()
        return self.board

        


       





        


       




