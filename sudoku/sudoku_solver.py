"""I am not necessarily copying from here, but I am basing my code on this video: https://www.youtube.com/watch?v=tvP_FZ-D9Ng
I really like the recursive and backtracking approach that this person took, and I tried to recreate it in part,
but I didn't want to just copy what she did. Additionally, she only created the sudoku_solver, not the maker."""

blank_puzzle = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]

#Pulled from a NYT-generated sudoku
easy_puzzle = [[1,5,9,2,3,0,0,0,0],
               [8,0,0,0,1,4,7,0,0],
               [4,0,0,5,0,0,3,1,0],
               [0,6,0,1,0,2,5,7,8],
               [0,0,2,0,8,3,0,0,0],
               [9,8,0,0,4,0,0,0,6],
               [0,0,5,0,0,0,8,2,3],
               [7,0,0,3,0,6,0,0,5],
               [0,9,3,0,0,0,0,6,7]]

#Pulled from a NYT-generated sudoku
medium_puzzle = [[0,1,0,0,0,0,0,0,0],
                 [0,2,0,0,0,0,0,8,0],
                 [3,4,6,0,0,1,0,0,7],
                 [0,0,2,0,3,0,0,0,0],
                 [4,0,3,0,0,0,7,0,1],
                 [6,7,0,1,0,0,9,0,0],
                 [0,0,0,7,6,0,0,0,0],
                 [0,0,0,8,0,0,0,6,3],
                 [0,0,0,2,0,0,8,0,0]]

#Pulled from a NYT-generated sudoku
hard_puzzle = [[8,0,0,4,7,0,5,0,0],
               [0,0,0,0,0,0,0,0,1],
               [7,0,0,0,0,0,0,8,0],
               [6,1,0,5,0,0,0,9,0],
               [0,0,4,0,9,0,2,1,0],
               [0,5,0,0,0,3,0,0,8],
               [0,0,7,3,0,6,1,0,0],
               [0,0,6,0,0,0,0,2,0],
               [0,0,0,0,0,0,3,0,0]]


def find_next_empty(puzzle):
    """Staring from the top left corner, this function scans through the rows from left to right 
    to find the next blank spot, represented with a 0."""
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                return row, column
    """If there is no blank square left to guess, then there we return None, None because there are 
    no more rows or columns to guess for."""
    return None, None

def is_valid(puzzle, guess, row, column):
    """This function determines whether a guess is valid for a blank square (where there is a 0).
    It checks for to see if the guess is already in the row, then the column, then the 3x3 box. 
    It either returns true or false."""

    #Check rows:
    row_values = puzzle[row]
    if guess in row_values:
        return False

    #Check columns:
    #Using a list comprehension to collect all the values in a column 
    column_values = [puzzle[i][column] for i in range(9)]

    # columns = [for column in row ]
    if guess in column_values:
        return False

    #Check 3x3's:
    #These allow us to find the start of the 3x3's.
    row3x3 = row // 3 * 3
    column3x3 = column // 3 * 3 

    grid3x3_values = []
    for r in range(row3x3, row3x3 + 3):
        for c in range(column3x3, column3x3 +3):
                grid3x3_values.append(puzzle[r][c])

    if guess in grid3x3_values:
        return False
    
    #If the row, column, and 3x3 grid checks pass, then return that the guess is a value option
    return True

def print_sudoku(puzzle):
    """Prints out the sudoku puzzle in a visually appealing way, showing blank squares with an underscore."""
    for i in range(9):
        if i % 3 == 0:
            print("+-----------------------+")
        for j in range(9):
            if j % 3 == 0:
                print("| ", end="")
            if puzzle[i][j] == 0:
                print("_ ", end="")
            else:
                print(f"{puzzle[i][j]} ", end="")
        print("|")
    print("+-----------------------+")

def solve_sudoku(puzzle):
    """This function uses backtracking and recrusion to solve a sudoku puzzle."""
    row, column = find_next_empty(puzzle)
    """This the base condition for the recursive strategy. If there are no more blank rows or 
    columns, then a valid solution has been found."""
    if row is None:
        return True
    
    for guess in range(1,10):
        #Checks if guess is valid and continues solving
        if is_valid(puzzle, guess, row, column):
            puzzle[row][column] = guess
            if solve_sudoku(puzzle):
                return True

        #Resets invalid guess
        puzzle[row][column] = 0
    
    return False

def main():
    puzzle = hard_puzzle.copy()
    if solve_sudoku(puzzle):
        print("Puzzle has been solved!")
        print_sudoku(puzzle)
    else:
        print("Puzzle is unsolvable.")

if __name__ == "__main__":
    main()
