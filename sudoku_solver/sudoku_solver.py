def find_next_empty(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle)):
            if(puzzle[row][col] == -1):
                return row, col
    return None, None

    # Return row, col tuple (or (None, None) if there is none)
    return (row, col)

def is_valid(puzzle, guess, row, col):
    # Returns true if its valid, False otherwise

    # Start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # Now with the columns
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    #Finally the 3x3 square 
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True


def sudoku_solver(puzzle):
    # Solving a Sudoku using Backtracking technique
    # Our puzzle is a list of list, where each inner list is a row in our sudoku puzzle
    # Return whether a solution exists 
    # Mutates puzzle to be the solution (if solution exists)

    # Step 1: Choose somewhere on the puzzle to make a guess 

    row, col = find_next_empty(puzzle)

    # Step 1.1: If there is nowhere left, then we are done, because we only allowed valid inputs. 
    if row == None:
        return True
    
    # Step 2: If there is a place to put a number, then put a guess between 1 and 9
    for guess in range(1,10):
        # Step 3: Check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # Step 3.1: If this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess

            # Now recurse using this puzzle

            # Step 4: recursively call our function
            if sudoku_solver(puzzle):
                return True
        # Step 5: If not valid OR if our guess does not solve the puzzle
        # Then we need to Backtrack and try a new number
        puzzle[row][col] = -1 # Reset the guess

    # Step 6: If none of the numbers that we try work, then this puzzle in UNSOLVABLE
    return False

if __name__ == '__main__':
    example_puzzle = [
        [ 3,  9, -1,   -1,  5, -1,   -1, -1, -1 ],
        [-1, -1, -1,    2, -1, -1,   -1, -1,  5 ],
        [-1, -1, -1,    7,  1, -1,   -1,  8, -1 ],

        [-1,  5, -1,   -1,  6,  8,   -1, -1, -1 ],
        [ 2, -1,  6,   -1, -1,  3,   -1, -1, -1 ],
        [-1, -1, -1,   -1, -1, -1,   -1, -1,  4 ],

        [ 5, -1, -1,   -1, -1, -1,   -1, -1, -1 ],
        [ 6,  7, -1,    1, -1,  5,   -1,  4, -1 ],
        [ 1, -1,  9,   -1, -1, -1,    2, -1, -1 ],
    ]
    print(sudoku_solver(example_puzzle))
    for row in example_puzzle:
        print(row)