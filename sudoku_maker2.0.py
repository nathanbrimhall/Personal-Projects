"""I am not necessarily copying from here, but I am basing my code on this video: https://www.youtube.com/watch?v=tvP_FZ-D9Ng
I really like the recursive and backtracking approach that this person took, and I tried to recreate it in part,
but I didn't want to just copy what she did. Additionally, she only created the sudoku_solver, not the maker."""

import random
import copy
import time
    
class SudokuPuzzle:
    def __init__(self, grid=None):
        if grid:
            self.grid = [row[:] for row in grid]
        else:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def find_next_empty(self):
        """Staring from the top left corner, this function scans through the rows from left to right 
        to find the next blank spot, represented with a 0."""
        for row in range(9):
            for column in range(9):
                if self.grid[row][column] == 0:
                    return row, column
                
        """If there is no blank square left to guess, then there we return None, None because there are 
        no more rows or columns to guess for."""
        return None, None
    
    def is_valid_guess(self, guess, row, column):
        """This function determines whether a guess is valid for a blank square (where there is a 0).
        It checks for to see if the guess is already in the row, then the column, then the 3x3 box. 
        It either returns true or false."""

        #Check rows:
        row_values = self.grid[row]
        if guess in row_values:
            return False

        #Check columns:
        #Using a list comprehension to collect all the values in a column 
        column_values = [self.grid[i][column] for i in range(9)]

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
                    grid3x3_values.append(self.grid[r][c])

        if guess in grid3x3_values:
            return False
        
        #If the row, column, and 3x3 grid checks pass, then return that the guess is a value option
        return True
    
    def print_sudoku(self):
        """Prints out the sudoku puzzle in a visually appealing way, showing blank squares with an underscore."""
        for i in range(9):
            if i % 3 == 0:
                print("+-----------------------+")
            for j in range(9):
                if j % 3 == 0:
                    print("| ", end="")
                if self.grid[i][j] == 0:
                    print("_ ", end="")
                else:
                    print(f"{self.grid[i][j]} ", end="")
            print("|")
        print("+-----------------------+")

    def remove_numbers(self, difficulty):
        """This function makes the necessary number of cells, according to the difficulty, blank for the user."""
        DIFFICULTY_GIVENS = {"easy": 40,
                            "medium": 32,
                            "hard": 24,
                            "test": 79}
        to_remove = 81 - DIFFICULTY_GIVENS.get(difficulty)

        cells = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells)
        for i in range(to_remove):
            r, c = cells[i]
            self.grid[r][c] = 0
        return
    
    def solve(self, guess_selector=None):
        """This function uses backtracking and recrusion to solve a sudoku puzzle."""
        row, column = self.find_next_empty()
        """This the base condition for the recursive strategy. If there are no more blank rows or 
        columns, then a valid solution has been found."""
        if row is None:
            return True
        
        """Here I am passing in an additional function for guess_selector. By default, it can solve 
        a puzzle with given values. With 'random_selector', it can create a random puzzle from a 0 
        grid, and the 'user_selector' allows the user to solve the puzzle."""
        if guess_selector is None:
            guesses = range(1, 10) #This default is set to the program solving a a puzzle with some given numbers
        else:
            guesses = guess_selector(row, column)

        for guess in guesses:
            #Checks if guess is valid and continues solving
            if self.is_valid_guess(guess, row, column):
                self.grid[row][column] = guess
                if self.solve(guess_selector):
                    return True

            #Resets invalid guess
            self.grid[row][column] = 0
        
        return False
    
    def random_selector(self, row, column):
        guesses = list(range(1,10))
        random.shuffle(guesses)
        return guesses
    
    # def user_selector(self, row, column):
    #     while True:
    #         try:
    #             guess = int(input(f"Enter your guess (1-9) for cell ({row+1}, {column+1}): "))
    #             if 1 <= guess <= 9:
    #                 return [guess]
    #         except ValueError:
    #             pass
    #         print("Invalid input. Try again.")

    def user_play(self):
        while True:
            self.print_sudoku()
            print("To quit, enter 'quit' at any prompt.")
            row = input("Enter row (1-9): ")
            if row == "quit":
                break
            col = input("Enter column (1-9): ")
            if col == "quit":
                break
            guess = input("Enter your guess (1-9): ")
            if guess == "quit":
                break
            try:
                row = int(row) - 1
                col = int(col) - 1
                guess = int(guess)
                if not (0 <= row < 9 and 0 <= col < 9 and 1 <= guess <= 9):
                    print("Invalid input. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Try again.")
                continue
            if self.grid[row][col] != 0:
                print("Cell is not empty. Try another cell.")
                continue
            if not self.is_valid_guess(guess, row, col):
                print("Invalid guess for this cell.")
                continue
            self.grid[row][col] = guess
            if all(0 not in row for row in self.grid):
                self.print_sudoku()
                print("Congratulations, you solved the puzzle!")
                break



def main():
    puzzle = SudokuPuzzle()
    puzzle.solve(guess_selector = puzzle.random_selector)
    key = copy.deepcopy(puzzle)
    
    difficulty = input("Type 'easy','medium',or 'hard' for a sudoku puzzle of that difficulty\nType 'quit' at any prompt to quit.\n")
    if difficulty == "quit":
        return
    
    #Checks that the difficult setting is valid
    if (difficulty != "easy" and difficulty != "medium" and difficulty != "hard" and difficulty != "test"):
        print("Invalid difficulty.")
        main()

    #Removes numbers from the key so user can solve the puzzle
    puzzle.remove_numbers(difficulty)    
    puzzle.print_sudoku()
    is_solved = False
    start_time = time.time()
    while is_solved == False:
        is_solved = puzzle.user_play()
        puzzle.print_sudoku()
        print("To quit, enter 'quit'.")

    #Calculates the time spent on solving the puzzle
    end_time = time.time()
    total_m = (end_time - start_time) // 60
    total_s = (end_time - start_time) % 60
    total_s = f"{total_s:.0f}"
    if len(total_s) == 1:
        total_s = f"0{total_s}"


    #Prints the key after the user is done solving the puzzle    
    key.print_sudoku()
    print("Nice job! Here is the key to your puzzle.")
    print(f"Your time was {total_m:.0f}:{total_s}.")
    

if __name__ == "__main__":
    main()
    
    