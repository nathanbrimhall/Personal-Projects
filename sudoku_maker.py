"""I am not necessarily copying from here, but I am basing my code on this video: https://www.youtube.com/watch?v=tvP_FZ-D9Ng
I really like the recursive and backtracking approach that this person took, and I tried to recreate it in part,
but I didn't want to just copy what she did. Additionally, she only created the sudoku_solver, not the maker."""

import sudoku_solver as ss
import random
import copy
import time
    

def generate_puzzle():
    #Provide a blank sudoku template:
    key = [[0 for _ in range(9)] for _ in range(9)]

    #Solve the blank template with random numbers so that a new puzzle is generated every time.
    solve_new_puzzle(key)
    return key

def solve_new_puzzle(new_puzzle):
    """This function uses backtracking and recrusion to solve a sudoku puzzle."""
    row, column = ss.find_next_empty(new_puzzle)
    """This the base condition for the recursive strategy. If there are no more blank rows or 
    columns, then a valid solution has been found."""
    if row is None:
        return True
    
    random.seed(1)
    guess_list = [1,2,3,4,5,6,7,8,9]
    while len(guess_list) != 0:
        guess = random.choice(guess_list)
        guess_list.remove(guess)
        #Checks if guess is valid and continues solving
        if ss.is_valid(new_puzzle, guess, row, column):
            new_puzzle[row][column] = guess
            if solve_new_puzzle(new_puzzle):
                return True

        #Resets invalid guess
        new_puzzle[row][column] = 0
    
    return False

def remove_numbers(new_puzzle, difficulty):
    EASY = 81-80 #40 are given, 41 are removed
    MEDIUM = 81-32 #32 are given, 49 are removed
    HARD = 81-24 #24 are given, 57 are removed
    if difficulty == "hard":
        given = HARD
    elif difficulty == "medium":
        given = MEDIUM
    else:
        given = EASY
    
    while given > 0:
        for row in range(9):
            for column in range(9):
                if new_puzzle[row][column] != 0:
                    remove_number = random.choice([True, False])
                    if remove_number and given > 0:
                        new_puzzle[row][column] = 0
                        given -= 1
    return new_puzzle

def read_input(is_solved, new_puzzle):
    #Allow the user to provide the coordinates of a cell to edit.
    row = input("Enter the row (1-9 from top to bottom).\n")
    if row == "quit":
        return True
    column = input("Enter the column (1-9 from left to right).\n")
    if column == "quit":
        return True
    user_guess = input(f"Enter your guess (1-9) for the cell ({row}, {column}).\n")
    if user_guess == "quit":
        return True
    
    row = int(row) - 1
    column = int(column) - 1
    user_guess = int(user_guess)
    #Set the cell value to 0 if it wasn't already 0.
    # if user_guess == 0 and new_puzzle[row][column] != 0:
    #     new_puzzle[row][column] = 0
    #     return is_solved
    
    #Validate that the cell is empty
    if new_puzzle[row][column] != 0:
        ss.print_sudoku(new_puzzle)
        print(f"INVALID INPUT ------> Cell ({row + 1}, {column + 1}) is not empty.")
        return is_solved
    
    #Validate that the guess is a valid guess
    elif not ss.is_valid(new_puzzle, user_guess, row, column) or not 1 <= user_guess <= 9:
        ss.print_sudoku(new_puzzle)
        print(f"INVALID INPUT ------> Guess ({user_guess}) for cell ({row + 1}, {column + 1}) is not valid.")
        return is_solved
    
    #All other guesses should be valid, so we will enter the inputted value
    else:
        new_puzzle[row][column] = user_guess
        #Checks if the puzzle is solved or not.
        for row in new_puzzle:
            if 0 not in row:
                # if win_condition(new_puzzle):
                is_solved = True
                # else:
                #     ss.print_sudoku(new_puzzle)
                #     print("It looks like your puzzle isn't correct.")
        ss.print_sudoku(new_puzzle)
        return is_solved

# def win_condition(new_puzzle, new_key):
#     new_puzzle = 

def main():
    #Creates a new puzzle key
    new_key = generate_puzzle() 
    new_puzzle = copy.deepcopy(new_key)
    
    difficulty = input("Type 'easy','medium',or 'hard' for a sudoku puzzle of that difficulty\nType 'quit' to quit.\n")
    if difficulty == "quit":
        return
    
    #Checks that the difficult setting is valid
    if (difficulty != "easy" and difficulty != "medium" and difficulty != "hard"):
        print("Invalid difficulty.")
        main()

    #Removes numbers from the key so user can solve the puzzle
    new_puzzle = remove_numbers(new_puzzle, "easy")    
    ss.print_sudoku(new_puzzle)

    is_solved = False
    start_time = time.time()
    while is_solved == False:
        is_solved = read_input(is_solved, new_puzzle)
        # ss.print_sudoku(new_puzzle)
        print("To quit, enter 'quit'.")

    #Calculates the time spent on solving the puzzle
    end_time = time.time()
    total_m = (end_time - start_time) // 60
    total_s = (end_time - start_time) % 60
    total_s = f"{total_s:.0f}"
    if len(total_s) == 1:
        total_s = f"0{total_s}"


    #Prints the key after the user is done solving the puzzle    
    ss.print_sudoku(new_key)
    print("Nice job! Here is the key to your puzzle.")
    print(f"Your time was {total_m:.0f}:{total_s}.")
    

if __name__ == "__main__":
    main()
    