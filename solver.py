"""TODO:
1) The code will be used to solve a sudoku.
"""
from input_sudoku import INPUT_SUDOKU, SUDOKU_SIZE

def check_sudoku_solved(sudoku:list):
    # unfilled_count = 0
    for row in sudoku:
        for value in row:
            if not (isinstance(value, int) and value in range(1,10)):
                return False
    return True

def remove_horizontal_occurences(sudoku_grid:list, possible_occurences:list, row:int, sudoku_len:int):
    for i in range(0, sudoku_len):
        if isinstance(sudoku_grid[row][i], int) and sudoku_grid[row][i] != 0 and sudoku_grid[row][i] in possible_occurences:
            possible_occurences.remove(sudoku_grid[row][i])
    return possible_occurences

def remove_vertical_occurences(sudoku_grid:list, possible_occurences:list, column:int, sudoku_len:int):
    for i in range(0, sudoku_len):
        if isinstance(sudoku_grid[i][column], int) and sudoku_grid[i][column] != 0 and sudoku_grid[i][column] in possible_occurences:
            possible_occurences.remove(sudoku_grid[i][column])
    return possible_occurences

def remove_mini_grid_occurences(sudoku_grid, possible_occurences, row, column):
    horizontal_start = SUDOKU_SIZE*int(row/SUDOKU_SIZE)
    horizontal_end = horizontal_start + SUDOKU_SIZE
    vertical_start = SUDOKU_SIZE*int(column/SUDOKU_SIZE)
    vertical_end = vertical_start + SUDOKU_SIZE
    for i in range(horizontal_start, horizontal_end):
        for j in range(vertical_start, vertical_end):
            if isinstance(sudoku_grid[i][j], int) and sudoku_grid[i][j] != 0 and sudoku_grid[i][j] in possible_occurences:
                possible_occurences.remove(sudoku_grid[i][j])
    return possible_occurences

def solve_sudoku(sudoku_grid):
    sudoku_len = SUDOKU_SIZE**2
    for i in range(0, sudoku_len):
        for j in range(0, sudoku_len):
            if isinstance(sudoku_grid[i][j], list):
                sudoku_grid[i][j] = remove_horizontal_occurences(sudoku_grid, sudoku_grid[i][j], i, sudoku_len)
                sudoku_grid[i][j] = remove_vertical_occurences(sudoku_grid, sudoku_grid[i][j], j, sudoku_len)
                sudoku_grid[i][j] = remove_mini_grid_occurences(sudoku_grid, sudoku_grid[i][j], i, j)
            elif sudoku_grid[i][j] == 0:
                temp_list = [z for z in range(1,10)]
                temp_list = remove_horizontal_occurences(sudoku_grid, temp_list, i, sudoku_len)
                temp_list = remove_vertical_occurences(sudoku_grid, temp_list, j, sudoku_len)
                temp_list = remove_mini_grid_occurences(sudoku_grid, temp_list, i, j)
                sudoku_grid[i][j] = temp_list
            if isinstance(sudoku_grid[i][j], list) and len(sudoku_grid[i][j]) == 1:
                print(f"Something found at {i+1}, {j+1} i.e = {sudoku_grid[i][j][0]}")
                sudoku_grid[i][j] = sudoku_grid[i][j][0]
    return sudoku_grid


for i in range(0,10):
    sudoku_solved = check_sudoku_solved(INPUT_SUDOKU)
    if sudoku_solved:
        print(sudoku_solved)
        break
    else:
        print("Sudoku not solved.")
        INPUT_SUDOKU = solve_sudoku(INPUT_SUDOKU)
for row in INPUT_SUDOKU:
    print(row)
