"""TODO:
1) The code will be used to solve a sudoku.
"""
from input_sudoku import INPUT_SUDOKU, SUDOKU_SIZE
import copy

def check_sudoku_solved(sudoku:list)-> int:
    unfilled_count = 0
    for row in sudoku:
        for value in row:
            if not (isinstance(value, int) and value in range(1, SUDOKU_SIZE**2+1)):
                unfilled_count += 1
    return unfilled_count

def remove_positional_horizontal_occurences(sudoku_grid:list, possible_occurences:list, row:int, sudoku_len:int):
    for i in range(0, sudoku_len):
        if isinstance(sudoku_grid[row][i], int) and sudoku_grid[row][i] != 0 and sudoku_grid[row][i] in possible_occurences:
            possible_occurences.remove(sudoku_grid[row][i])
    return possible_occurences

def remove_positional_vertical_occurences(sudoku_grid:list, possible_occurences:list, column:int, sudoku_len:int):
    for i in range(0, sudoku_len):
        if isinstance(sudoku_grid[i][column], int) and sudoku_grid[i][column] != 0 and sudoku_grid[i][column] in possible_occurences:
            possible_occurences.remove(sudoku_grid[i][column])
    return possible_occurences

def remove_positional_mini_grid_occurences(sudoku_grid, possible_occurences, row, column):
    horizontal_start = SUDOKU_SIZE*int(row/SUDOKU_SIZE)
    horizontal_end = horizontal_start + SUDOKU_SIZE
    vertical_start = SUDOKU_SIZE*int(column/SUDOKU_SIZE)
    vertical_end = vertical_start + SUDOKU_SIZE
    for i in range(horizontal_start, horizontal_end):
        for j in range(vertical_start, vertical_end):
            if isinstance(sudoku_grid[i][j], int) and sudoku_grid[i][j] != 0 and sudoku_grid[i][j] in possible_occurences:
                possible_occurences.remove(sudoku_grid[i][j])
    return possible_occurences

def remove_horizontal_occurences(sudoku_grid, val_to_remove, row, sudoku_len):
    for i in range(0, sudoku_len):
        if isinstance(sudoku_grid[row][i], list) and val_to_remove in sudoku_grid[row][i]:
            sudoku_grid[row][i].remove(val_to_remove)
    return sudoku_grid

def remove_vertical_occurences(sudoku_grid, val_to_remove, column, sudoku_len):
    for i in range(0, sudoku_len):
        if isinstance(sudoku_grid[i][column], list) and val_to_remove in sudoku_grid[i][column]:
            sudoku_grid[i][column].remove(val_to_remove)
    return sudoku_grid

def remove_mini_grid_occurences(sudoku_grid, val_to_remove, row, column):
    horizontal_start = SUDOKU_SIZE*int(row/SUDOKU_SIZE)
    horizontal_end = horizontal_start + SUDOKU_SIZE
    vertical_start = SUDOKU_SIZE*int(column/SUDOKU_SIZE)
    vertical_end = vertical_start + SUDOKU_SIZE
    for i in range(horizontal_start, horizontal_end):
        for j in range(vertical_start, vertical_end):
            if isinstance(sudoku_grid[i][j], list) and val_to_remove in sudoku_grid[i][j]:
                sudoku_grid[i][j].remove(val_to_remove)
    return sudoku_grid

def solve_horizontal_single_occurences(sudoku_grid:list, row:int, sudoku_len:int):
    for check_val in range(1, SUDOKU_SIZE**2+1):
        single_occurence_column = None
        occurence_count = 0
        for i in range(0, sudoku_len):
            if isinstance(sudoku_grid[row][i],list) and check_val in sudoku_grid[row][i]:
                occurence_count +=1
                if occurence_count >1:
                    break
                single_occurence_column = i
        if occurence_count == 1:
            #as we found a single occurence in horizontal remove occurences in vertical
            sudoku_grid = remove_vertical_occurences(sudoku_grid, check_val, single_occurence_column, sudoku_len)
            sudoku_grid = remove_mini_grid_occurences(sudoku_grid, check_val, row, single_occurence_column)
            # for j in range(0, sudoku_len):
            #     if isinstance(sudoku_grid[j][single_occurence_column],list) and check_val in sudoku_grid[j][single_occurence_column]:
            #         sudoku_grid[j][single_occurence_column].remove(check_val)
            print(f"Medium horizontal find at {row+1}, {single_occurence_column+1} i.e {check_val}.")
            sudoku_grid[row][single_occurence_column] = check_val
    return sudoku_grid

def solve_vertical_single_occurences(sudoku_grid, column:int, sudoku_len:int):
    for check_val in range(1, SUDOKU_SIZE**2+1):
        single_occurence_row = None
        occurence_count = 0
        for i in range(0, sudoku_len):
            if isinstance(sudoku_grid[i][column],list) and check_val in sudoku_grid[i][column]:
                occurence_count +=1
                if occurence_count >1:
                    break
                single_occurence_row = i
        if occurence_count == 1:
            sudoku_grid = remove_horizontal_occurences(sudoku_grid, check_val, single_occurence_row, sudoku_len)
            sudoku_grid = remove_mini_grid_occurences(sudoku_grid, check_val, single_occurence_row, column)
            # for j in range(0, sudoku_len):
            #     if isinstance(sudoku_grid[single_occurence_row][j],list) and check_val in sudoku_grid[single_occurence_row][j]:
            #         sudoku_grid[single_occurence_row][j].remove(check_val)
            print(f"Medium vertical find at {single_occurence_row+1}, {column+1} i.e {check_val}.")
            sudoku_grid[single_occurence_row][column] = check_val
    return sudoku_grid

def solve_mini_grid_single_occurence(sudoku_grid, row, column, sudoku_len):
    horizontal_start = SUDOKU_SIZE*int(row/SUDOKU_SIZE)
    horizontal_end = horizontal_start + SUDOKU_SIZE
    vertical_start = SUDOKU_SIZE*int(column/SUDOKU_SIZE)
    vertical_end = vertical_start + SUDOKU_SIZE
    for check_val in range(1, SUDOKU_SIZE**2+1):
        single_occurence_row = None
        single_occurence_column = None
        occurence_count = 0
        for i in range(horizontal_start, horizontal_end):
            for j in range(vertical_start, vertical_end):
                if isinstance(sudoku_grid[i][j],list) and check_val in sudoku_grid[i][j]:
                    occurence_count +=1
                    if occurence_count >1:
                        break
                    single_occurence_row = i
                    single_occurence_column = j
            if occurence_count >1:
                break
        if occurence_count == 1:
            sudoku_grid = remove_horizontal_occurences(sudoku_grid, check_val, single_occurence_row, sudoku_len)
            sudoku_grid = remove_vertical_occurences(sudoku_grid, check_val, single_occurence_column, sudoku_len)
            print(f"Medium grid find at {single_occurence_row+1}, {single_occurence_column+1} i.e {check_val}.")
            sudoku_grid[single_occurence_row][single_occurence_column] = check_val
    return sudoku_grid

def solve_sudoku(sudoku_grid):
    sudoku_len = SUDOKU_SIZE**2

    # generic rules horizontal, vertical and mini grid checker. 
    for i in range(0, sudoku_len):
        for j in range(0, sudoku_len):
            if sudoku_grid[i][j] == 0:
                temp_list = [z for z in range(1,sudoku_len+1)]
                temp_list = remove_positional_horizontal_occurences(sudoku_grid, temp_list, i, sudoku_len)
                temp_list = remove_positional_vertical_occurences(sudoku_grid, temp_list, j, sudoku_len)
                temp_list = remove_positional_mini_grid_occurences(sudoku_grid, temp_list, i, j)
                sudoku_grid[i][j] = temp_list
            elif isinstance(sudoku_grid[i][j], list):
                sudoku_grid[i][j] = remove_positional_horizontal_occurences(sudoku_grid, sudoku_grid[i][j], i, sudoku_len)
                sudoku_grid[i][j] = remove_positional_vertical_occurences(sudoku_grid, sudoku_grid[i][j], j, sudoku_len)
                sudoku_grid[i][j] = remove_positional_mini_grid_occurences(sudoku_grid, sudoku_grid[i][j], i, j)
            if isinstance(sudoku_grid[i][j], list) and len(sudoku_grid[i][j]) == 1:
                print(f"Something found at {i+1}, {j+1} i.e = {sudoku_grid[i][j][0]}")
                sudoku_grid[i][j] = sudoku_grid[i][j][0]
                sudoku_grid = remove_horizontal_occurences(sudoku_grid, sudoku_grid[i][j], i, sudoku_len)
                sudoku_grid = remove_vertical_occurences(sudoku_grid, sudoku_grid[i][j], j, sudoku_len)
                sudoku_grid = remove_mini_grid_occurences(sudoku_grid, sudoku_grid[i][j], i, j)
        
    # mediocer level fill info, based on single time occurence in vertical or horizontal or mini grid.
    for i in range(0, sudoku_len):
        sudoku_grid = solve_horizontal_single_occurences(sudoku_grid, i, sudoku_len)
        sudoku_grid = solve_vertical_single_occurences(sudoku_grid, i, sudoku_len)
        if i%3==0:
            for j in range(0, sudoku_len, 3):
                sudoku_grid = solve_mini_grid_single_occurence(sudoku_grid, i, j, sudoku_len)
        # remove mini grid single occurence
    return sudoku_grid

old_unsolved_places = None
while(True): 
    unsolved_places = check_sudoku_solved(INPUT_SUDOKU)
    if unsolved_places == 0:
        print("Sudoku Solved")
        break
    elif old_unsolved_places is not None and old_unsolved_places == unsolved_places:
        print("The sudoku cant be solved!!!")
        break
    else:
        print("Sudoku not solved.")
        INPUT_SUDOKU = solve_sudoku(INPUT_SUDOKU)
    old_unsolved_places = unsolved_places
    for row in INPUT_SUDOKU:
        print(row)
