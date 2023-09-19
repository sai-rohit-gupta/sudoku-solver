"""TODO:
1) The code will be used to solve a sudoku.
"""
from input_sudoku import INPUT_SUDOKU, SUDOKU_SIZE

def check_sudoku_solved(sudoku:list):
    zero_count = 0
    for row in sudoku:
        zero_count += row.count(0)
        if zero_count>0:
            break
    if zero_count>0:
        return True
    else:
        return False

# def remove_horizontal_occurences(sudoku_grid, possible_occurences, row, column, sudoku_len):
#     for i in range(0, sudoku_len):
#         if 

def solve_sudoku(sudoku_grid):
    sudoku_len = SUDOKU_SIZE^2
    for i in range(0, sudoku_len):
        for j in range(0, sudoku_len):
            if isinstance(sudoku_grid[i][j], list):
                pass
            elif sudoku_grid[i][j] == 0:
                temp_list = [z for z in range(1,10)]
                temp_list = remove_horizontal_occurences(sudoku_grid, temp_list, i, j, sudoku_len)
                temp_list = remove_vertical_occurences(sudoku_grid, temp_list, i, j, sudoku_len)
                temp_list = remove_mini_grid_occurences(sudoku_grid, temp_list, i, j)
                

sudoku_solved, sudoku_grid = check_sudoku_solved(INPUT_SUDOKU)
if sudoku_solved:
    print(sudoku_grid)
else:
    print("Sudoku not solved.")
    print(sudoku_grid)
