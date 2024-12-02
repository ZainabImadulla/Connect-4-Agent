# Board.py
# Represents a board in a game of connect 4
import copy
import math
import random
import numpy as np

class Board:
    def __init__(self, board=None):
        if(board == None):
            self.board = [[0] * 7 for i in range(6)]
        else:
            self.board = copy.deepcopy(board)


    def add_coin(self, column, player):
        for i in range(5, -1, -1):
            if not self.has_any_coin(i, column):
                self.board[i][column] = player
                break
        
    def move_possible(self, column):
        if column > 6 or column < 0:
            return False
        possible = False
        for i in range(5, -1, -1):
            possible = possible or not self.has_any_coin(i, column)
        
        return possible

    def has_specific_coin(self, row, column, player):
        if self.board[row][column] == player:
            return True
        return False
    
    def has_any_coin(self, row, column):
        if self.board[row][column] == 0:
            return False
        return True
    
    def check_won(self, player):
        return self.check_vertical(player) or self.check_horizontal(player) or self.check_diagonal(player)

    
    def is_board_full(self):
        for i in range(7):
            for j in range(6):
                if self.board[j][i] == 0:
                    return False
        return True  
    
    def terminal_state(self):
        return self.is_board_full() or self.check_won(1) or self.check_won(2)


    def check_vertical(self, player):
        for x in range(7):
            count = 0
            for y in range(6):
                if self.has_specific_coin(y, x, player):
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
        return False
                
    def check_horizontal(self, player):
        for x in range(6):
            count = 0
            for y in range(7):
                if self.has_specific_coin(x, y, player):
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
        return False

    def check_diagonal(self, player):
        for f in range(3, 6):
            count = 0
            x = 0
            for z in range(f, -1, -1):
                if self.has_specific_coin(z, x, player) :
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
                x += 1
            if count >= 4:
                return True
        
        for f in range(1, 4):
            count = 0
            y = 5
            for z in range(f, 6):
                if self.has_specific_coin(y, z, player):
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
                y -= 1
            if count >= 4:
                return True


        for f in range(3, 6):
            count = 0
            x = 6
            for z in range(f, -1, -1):
                if self.has_specific_coin(z, x, player):
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
                x -= 1
            if count >= 4:
                return True

        for f in range(3, 7):
            count = 0
            y = 5
            for z in range(f, -1, -1):
                if self.has_specific_coin(y, z, player):
                    count += 1
                    if count == 4:
                        return True
                else: 
                    count = 0
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

    def eval_function(self, player):
        score = 0
        opponent = 3 - player

        eval_board = np.array(
                    [[3, 4, 5, 7, 5, 4, 3],
                    [4, 6, 8, 10, 8, 6, 4],
                    [5, 7, 11, 13, 11, 7, 5],
                    [5, 7, 11, 13, 11, 7, 5],
                    [4, 6, 8, 10, 8, 6, 4],
                    [3, 4, 5, 7, 5, 4, 3]])
        
        player_score = np.sum(eval_board[self.board == player])
        opponent_score = np.sum(eval_board[self.board == opponent])
        score = player_score - opponent_score
        return score
    
    def minimax(self, depth, alpha, beta, maximizing_turn, player):
        opponent = 3 - player
        next_states = self.generate_next_states(player) 
        terminal = self.terminal_state()


        if depth == 0 or terminal:
            if terminal:
                if self.check_won(player):
                    return (self, math.inf)
                elif self.check_won(opponent):
                    return (self, -math.inf)
                else: 
                    return (self, 0)
        else:
            return (self, self.eval_function(player))
        
        if maximizing_turn:
            value = -math.inf
            next_state = random.choice(next_states)
            for state in next_states:
                new_score = state.minimax(depth - 1, alpha, beta, False)[1]
            
                if new_score > value:
                    value = new_score
                    next_state = state
                alpha = max(alpha, value)

                if alpha >= beta:
                    break
            return next_state, value
        
        else:
            value = math.inf
            next_state = random.choice(next_states)
            for state in next_states:
                new_score = state.minimax(depth - 1, alpha, beta, True)[1]

                if new_score < value:
                    value = new_score
                    next_state = state
                    beta = min(beta, value)

                if alpha >= beta:
                    break
            return next_state, value
