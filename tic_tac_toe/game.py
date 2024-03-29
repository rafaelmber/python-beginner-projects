from player import RandomComputerPlayer, HumanPlayer, GeniusComputerPlayer
import math
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use a single list to rep a 3x3 board
        self.current_winner = None # Keep track of winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row) + '|')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (Tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' |'.join(row) + ' |')
    
    def available_moves(self):
        # Comprehensive version
        return [i for (i,spot) in enumerate(self.board) if spot == ' ']
        # Long version
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     # ['X','X','O'] -> [(0,'X'), (1,'X'), (2,'O')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
    def empty_squares(self):
        return ' ' in self.board
    
    def number_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # If valid move then make the move, then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False
    
    def winner(self, square, letter):
        # Winner if 3 in a row anywhere
        
        # First let's check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check columns
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals 
        # But only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only possible moves to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # Starting letter

    # Iterate while the game has empty squares
    # When a player wins the loop will break
    
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Define a function to make a move
        if game.make_move(square, letter): 
            if (print_game):
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                    return letter
            
            letter = 'O' if letter == 'X' else 'X'
        # Little delay
        time.sleep(0.8)

    if print_game:
        print('It\' a tie')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')

    game = TicTacToe()

    play(game, x_player, o_player, True)