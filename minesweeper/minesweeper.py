import random
import re
# Lets create a board object to represent the minesweeper game
# This is so that we can just say "Create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Let's create the board
        self.board = self.make_new_board() # Plant the bombs
        self.assign_values_to_board()


        # Initialize a set to keep track of which locations we've uncovered
        # We'll say (row, col) tuples into this set 
        self.dug = set()
    
    def make_new_board(self):
        # Construct a new board based on the dim size and num bombs
        # we should construct the list of lists here

        # Generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # Plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*': # * represents a bomb
                continue

            board[row][col] = '*'
            bombs_planted += 1
        
        return board
    
    def assign_values_to_board(self):
        # Assign a number 0-8 for all the empty spaces representing how many neighboring bombs there are
        # We can precompute this and it will save us some effort checking what is around the board later on

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self, row, col):
        # Let's iterate through each of the neighboring positions and sum number of bombs

        # Make sure not to go out of bounds

        num_neighboring_bombs = 0
        for r in range(max(0,row-1), min(self.dim_size, (row + 1) + 1)):
            for c in range(max(0,col - 1), min(self.dim_size,(col + 1) + 1)):
                if r == row and c == col:
                    # Original position, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs
    
    def dig(self, row, col):
        # Dig at that location
        # Return True if successful dig, False if bomb dug

        # A few scenarios
        # Hit a bomb -> game over
        # Dig a location with neighboring bombs -> finish dig
        # Dig a location with no neighboring bombs -> recursively dig neighbors

        self.dug.add((row, col)) # keep track that we dug here
        
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0
        for r in range(max(0,row-1), min(self.dim_size, (row + 1) + 1)):
            for c in range(max(0,col - 1), min(self.dim_size,(col + 1) + 1)):
                if (r,c) in self.dug:
                    continue # Don't dig where you already dug
                self.dig(r,c)

        return True

    def __str__(self):
        # This is a magic function where if you call print on this object
        # I'll print out what this function returns. 
        # Return a string that shows the board to the player

        # First, let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # Put this together in a string
        output = ''
        for row in visible_board:
            output = output + '\n' + ('|' + ' |'.join(row) + ' |')

        return  output

def play(dim_size = 10, num_bombs= 10):
    # Step 1: Create the board and plant the bombs
    board = Board(dim_size, num_bombs)


    # Step 2: Show the user the board and ask for where they want to dig

    # Step 3a: if location is a bomb, show game over message
    # Step 3: if location is not a bomb, dig recursively until each square is at least next to a bomb 
    # Step 4: Repeat step 2 and steps 3a/b until there are no more places to dig -> Victory 

    safe = True

    while len(board.dug) < board.dim_size**2 - board.num_bombs:
        print(board)
        user_input = re.split(',(\\s)*',input('Where would you like to dig? Input as row,col: '))
        row, col = int(user_input[0]), int(user_input[-1])

        if (row < 0 or row >= board.dim_size) or (col < 0 or col >= board.dim_size):
            print('Invalid location. Try again')
            continue

        safe = board.dig(row, col)

        if not safe:
            # Dug a bomb
            break
    
    if safe:
        print('Congratulations, You won')
    else:
        print('You lose')
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play(10,10)
