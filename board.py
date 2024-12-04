# Board.py
# Represents a board in a game of connect 4
import copy
import math
import random

class Board:
    def __init__(self, board=None):
        if(board == None):
            self.board = [[0] * 7 for i in range(6)]
        else:
            self.board = copy.deepcopy(board)

    # add_coin method adds a coin of the given player in the given column 
    def add_coin(self, column, player):
        for i in range(5, -1, -1):
            if not self.has_any_coin(i, column):
                self.board[i][column] = player
                break

    # method move_possible checks if a move is possible by checking that the column is valid and has space
    def move_possible(self, column):
        if column > 6 or column < 0:
            return False
        possible = False
        for i in range(5, -1, -1):
            possible = possible or not self.has_any_coin(i, column)
        return possible

    # method has_specific_coin returns true is the coin at the given row, column index is the given player (from method param)
    def has_specific_coin(self, row, column, player):
        if self.board[row][column] == player:
            return True
        return False
    
    # method has_any_coin returns true if any coin (doesn't matter which player) is at the given row, column index
    def has_any_coin(self, row, column):
        if self.board[row][column] == 0:
            return False
        return True
    
    # method check_won returns true if the given player has won the board by checking all vertical, horizontal, and diagonal possibilities
    def check_won(self, player):
        return self.check_vertical(player) or self.check_horizontal(player) or self.check_diagonal(player)

    # method is_board_full checks if the board has any empty spots, returns true if so, and false otherwise 
    def is_board_full(self):
        for i in range(7):
            for j in range(6):
                if self.board[j][i] == 0:
                    return False
        return True  
    
    # method check_vertical will check all vertical columns for 4 coins in a row of the player given by the parameter
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
                
    # method check_horizontal will check all horizontal rows for 4 coins in a row of the player given by the parameter
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

    # method check_diagonal_top_left checks if there are any 4 coins in a diagonal row 
    # of the given player in the top left portion of the board
    def check_diagonal_top_left(self, player):
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
        return False
    
    # method check_diagonal_bottom_left checks if there are any 4 coins in a diagonal row 
    # of the given player in the bottom left portion of the board   
    def check_diagonal_bottom_left(self, player):
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
        return False
    
    # method check_diagonal_top_right checks if there are any 4 coins in a diagonal row 
    # of the given player in the top right portion of the board
    def check_diagonal_top_right(self, player):
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
        return False
    
    # method check_diagonal_bottom_right checks if there are any 4 coins in a diagonal row 
    # of the given player in the bottom right portion of the board
    def check_diagonal_bottom_right(self, player):
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


    # method check_diagonal will check all diagonal paths for 4 coins in a row of the player given by the parameter
    def check_diagonal(self, player):
        return self.check_diagonal_top_left(player) or self.check_diagonal_bottom_left(player) or self.check_diagonal_top_right(player) or self.check_diagonal_bottom_right(player)

        
    
    # method generate_possible_moves will give a list of all possible rows that could be the next move in the game
    def generate_possible_moves(self):
        possible_moves = []
        for col in range(7):
            if self.move_possible(col):
                possible_moves.append(col)
        return possible_moves
        
    # method print_board prints the board to the output (used for debugging and testing)
    def print_board(self):
        for i in range(6):
            for j in range(7):
                print(self.board[i][j],  end=" ")
            print()

    # method getBoard returns the board
    def getBoard(self):
        return self.board
    
    # method in_a_row_horizontal returns the number of times the given player from the parameter has 
    # given num parameter number coins in a horizontal row with one space next to or between the num coins 
    # the empty space is used to track whether it would be a possible move to build off of this num coins
    def in_a_row_horizontal(self, player, num):
        total_num_in_row = 0
        count = 0
        empty_space = 0
        starting_empty_space = 0
        for row in range(6):
            for i in range(7):
                if self.board[row][i] == player:
                    count += 1
                    if count >= num and empty_space >= 1:
                        total_num_in_row += 1
                        empty_space = 0
                        
                elif self.board[row][i] == (3 - player):
                    count = 0
                    empty_space = 0
                elif self.board[row][i] == 0:
                    empty_space += 1
                    if empty_space >= 2:
                        count = 0
                    if count >= num and empty_space == 1:
                        total_num_in_row += 1
                        count = 0
            empty_space = 0
            count = 0
        return total_num_in_row
    
    # method in_a_row_vertical returns the number of times the given player from the parameter has 
    # given num parameter number coins in a vertical column with one space next to or between the num coins 
    # the empty space is used to track whether it would be a possible move to build off of this num coins
    def in_a_row_vertical(self, player, num):
        total_num_in_row = 0
        count = 0
        empty_space = 0
        for column in range(7) :
            for i in range(6):
                if self.board[i][column] == player:
                    count += 1
                    if count >= num and empty_space >= 1:
                        total_num_in_row += 1
                        empty_space = 0
                elif self.board[i][column] == (3 - player):
                    count = 0
                    empty_space = 0
                elif self.board[i][column] == 0:
                    empty_space += 1
                    if empty_space >= 2:
                        count = 0
                    if count >= num and empty_space >= 1:
                        total_num_in_row += 1
                        count = 0
            empty_space = 0
            count = 0
        return total_num_in_row
    
    # method diagonal_top_left calculates the number of num coins of specific player in a diagonal row within the top
    # left portion of the board
    def diagonal_top_left(self, player, num, opponent, total_num_in_row):
        for f in range(3, 6):
            count = 0
            empty_space = 0
            x = 0
            for z in range(f, -1, -1):
                if self.has_specific_coin(z, x, player) :
                    count += 1
                    if count >= num and empty_space >= 1:
                        total_num_in_row += 1
                        empty_space = 0
                elif self.has_specific_coin(z, x, opponent):
                    count = 0
                    empty_space = 0
                elif not self.has_any_coin(z, x):
                    empty_space += 1
                    if empty_space >= 2:
                        count = 0
                    if count >= num and empty_space >= 1:
                        total_num_in_row += 1
                        count = 0
                x += 1
        return total_num_in_row
    
    # method diagonal_bottom_left calculates the number of num coins of specific player in a diagonal row within the bottom
    # left portion of the board
    def diagonal_bottom_left(self, player, num, opponent, total_num_in_row):
        for f in range(1, 4):
            count = 0
            empty_space = 0
            y = 5
            for z in range(f, 6):
                if self.has_specific_coin(y, z, player):
                    count += 1
                    if count >= num and empty_space >= 1:
                        total_num_in_row += 1
                        empty_space = 0
                elif self.has_specific_coin(y, z, opponent):
                    count = 0
                    empty_space = 0
                elif not self.has_any_coin(y, z):
                    empty_space += 1
                    if empty_space >= 2:
                        count = 0
                    if count >= num and empty_space >= 1:
                        total_num_in_row += 1
                        count = 0
                y -= 1
        return total_num_in_row
    
     # method diagonal_top_right calculates the number of num coins of specific player in a diagonal row within the top
    # right portion of the board
    def diagonal_top_right(self, player, num, opponent, total_num_in_row):
        for f in range(3, 6):
            count = 0
            empty_space = 0
            x = 6
            for z in range(f, -1, -1):
                if self.has_specific_coin(z, x, player):
                    count += 1
                    if count >= num and empty_space >= 1:
                        total_num_in_row += 1
                        empty_space = 0
                elif self.has_specific_coin(z, x, opponent):
                    count = 0
                    empty_space = 0
                elif not self.has_any_coin(z, x):
                    empty_space += 1
                    if empty_space >= 2:
                        count = 0
                    if count >= num and empty_space >= 1:
                        total_num_in_row += 1
                        count = 0
                x -= 1
        return total_num_in_row
    
    # method diagonal_bottom_right calculates the number of num coins of specific player in a diagonal row within the bottom
    # right portion of the board
    def diagonal_bottom_right(self, player, num, opponent, total_num_in_row):
        for f in range(3, 7):
            count = 0
            empty_space = 0
            y = 5
            for z in range(f, -1, -1):
                if self.has_specific_coin(y, z, player):
                    count += 1
                    if count >= num and empty_space >= 1:
                        total_num_in_row += 1
                        empty_space = 0
                elif self.has_specific_coin(y, z, opponent):
                    count = 0
                    empty_space = 0
                elif not self.has_any_coin(y, z):
                    empty_space += 1
                    if empty_space >= 2:
                        count = 0
                    if count >= num and empty_space >= 1:
                        total_num_in_row += 1
                        count = 0
                y -= 1
        return total_num_in_row


    
    # method in_a_row_diagonal returns the number of times the given player from the parameter has 
    # given num parameter number coins in a diagonal path with one space next to or between the num coins, 
    # the empty space is used to track whether it would be a possible move to build off of this num coins   
    def in_a_row_diagonal(self, player, num):
        opponent = 3 - player
        total_num_in_row = 0
        top_left = self.diagonal_top_left(player, num, opponent, total_num_in_row)
        bottom_left = self.diagonal_bottom_left(player, num, opponent, total_num_in_row)
        top_right = self.diagonal_top_right(player, num, opponent, total_num_in_row)
        bottom_right = self.diagonal_bottom_right(player, num, opponent, total_num_in_row)
        total_num_in_row += top_left + bottom_left + top_right + bottom_right
        return total_num_in_row
    
    # method weigh_current_connections gets the weight of the given player by checking how many
    # 2s, 3s, and 4s the player has in their current state, this is a helper method for eval_func
    # (also abstracts duplicate code)
    def weigh_current_connections(self, player, is_opponent, type):
        score = 0
        # current heuristic slightly prioritizes offensive moves
        if type == "offensive":
            three_weight = 70
            if is_opponent:
                three_weight = 30
        
        elif type == "defensive":
            three_weight = 30
            if is_opponent:
                three_weight = 70
        
        # calculate all 2s, 3s, and 4s in all directions, multiply by weights, and sum together
        two_diagonal = 10 * self.in_a_row_diagonal(player, 2)
        three_diagonal = three_weight * self.in_a_row_diagonal(player, 3)
        four_diagonal = 1000000 * self.in_a_row_diagonal(player, 4)
        two_vertical = 10 * self.in_a_row_vertical(player, 2)
        three_vertical = three_weight * self.in_a_row_vertical(player, 3)
        four_vertical = 1000000 * self.in_a_row_vertical(player, 4)
        two_horizontal = 10 * self.in_a_row_horizontal(player, 2)
        three_horizontal = three_weight * self.in_a_row_horizontal(player, 3)
        four_horizontal = 1000000 * self.in_a_row_horizontal(player, 4)
        score += two_diagonal + two_horizontal + two_vertical
        score += three_diagonal + three_horizontal + three_vertical
        score += four_diagonal + four_horizontal + four_vertical
        return score


    # method center_weights gives each player a utility measure based on their spot relative to the center
    def center_weight(self, player):
        opponent = 3 - player
        player_score = 0
        opponent_score = 0

         # set and apply weight for prioritizing center moves
        eval_board = Board(
                    [[3, 4, 5, 7, 5, 4, 3],
                    [4, 6, 8, 10, 8, 6, 4],
                    [5, 7, 11, 13, 11, 7, 5],
                    [5, 7, 11, 13, 11, 7, 5],
                    [4, 6, 8, 10, 8, 6, 4],
                    [3, 4, 5, 7, 5, 4, 3]])
        player_score = 0
        opponent_score = 0

        for i in range(7):
            for j in range(6):
                if self.board[j][i] == player:
                    player_score += eval_board.board[j][i]
                elif self.board[j][i] == opponent:
                    opponent_score += eval_board.board[j][i]
        
        return player_score, opponent_score

    # method eval_function is used as a heuristic method to evaluate a given players board state
    # this method uses center weights as well as weighing how many 2 in a row, 3 in a row, and 4 in a row,
    # are present for the player and the opponent to evaluate the players state relative to its opponent
    def eval_function(self, player, type):
        score = 0
        opponent = 3 - player

        # all heuristics will always consider center weights
        player_score, opponent_score = self.center_weight(player)

        # if the heuristic type is not just center we will consider connections on the board
        # and whether to be offensive or defensive, based on the type
        if type != "center":
            # add weights for 2s, 3s, and 4s, in a row for both players and opponents
            player_score += self.weigh_current_connections(player, False, type)
            opponent += self.weigh_current_connections(opponent, True, type)
        score = player_score - opponent_score
        return score
    
    # method minimax produces the best next column to move to using 
    # the Minimax algorithm with Alpha-Beta pruning to evaluate all possible next moves.
    # Our algorithm alternates between maximizing and minimizing player   
    # strategies to determine the best possible move. It also uses recursive depth-limited search to
    # explore game states, evaluates terminal states using our eval_function, and incorporates Alpha-Beta pruning to optimize
    # the search by eliminating branches that cannot influence the final decision.
    def minimax(self, depth, alpha, beta, maximizing_turn, player, type):
        opponent = 3 - player
        possible_moves = self.generate_possible_moves() 

        # checking terminal states: if we're either player is won, we're at a draw, or if we've reached the depth limit
        if self.check_won(player):
            return None, math.inf
        elif self.check_won(opponent):
            return None, -math.inf
        elif self.is_board_full(): 
            return None, 0
        elif depth == 0:
            return None, self.eval_function(player, type)
    
        # maximizing turn
        if maximizing_turn:
            score = -math.inf # initialize best score to lowest value to get max score
            next_move = random.choice(possible_moves) # initialize to random column to start
            # iterate through possible moves and recursively call minimax alternating whether its the maximizing players turn
            for move in possible_moves:
                state = Board(self.board)
                state.add_coin(move, player)
                new_score = state.minimax(depth - 1, alpha, beta, False, player, type)[1]
            
                # update the best score and move if the new score is better
                if new_score > score:
                    score = new_score
                    next_move = move
                # update alpha
                alpha = max(alpha, score)

                # prune branches if alpha is no longer less than beta.
                if alpha >= beta:
                    break

            return next_move, score
        
        else:
            score = math.inf # initialize best score to highest value to get min score
            next_move = random.choice(possible_moves)  # initialize to random column to start
            # iterate through possible moves and recursively call minimax alternating whether its the maximizing players turn
            for move in possible_moves: 
                state = Board(self.board)
                state.add_coin(move, opponent)
                new_score = state.minimax(depth - 1, alpha, beta, True, player, type)[1]

                 # update the best score and move if the new score is better
                if new_score < score:
                    score = new_score
                    next_move = move
                # update beta
                beta = min(beta, score)
                
                # prune branches if alpha is no longer less than beta.
                if alpha >= beta:
                    break
            return next_move, score

    # Makes a random valid move 
    def random_move(self):
        while(True):
            random_number = random.randint(0, 6)
            if(self.move_possible(random_number)):
                return random_number
    
        
