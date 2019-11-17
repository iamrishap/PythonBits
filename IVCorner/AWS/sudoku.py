"""
Interview Problem: Sudoku Validator  
Requirements: 
each row contains digits 1 to 9, each digit occurs only once 
each col contains digits 1 to 9, each digit occurs only once 
each sub - grid(3 x3) contains digits 1 to 9, each digit occurs only once  
For example, here is a valid grid which should 
return true:  
int sudokuGrid = 
[[5, 3, 4, 6, 7, 8, 9, 1, 2], 
[6, 7, 2, 1, 9, 5, 3, 4, 8], 
[1, 9, 8, 3, 4, 2, 5, 6, 7], 
[8, 5, 9, 7, 6, 1, 4, 2, 3], 
[4, 2, 6, 8, 5, 3, 7, 9, 1], 
[7, 1, 3, 9, 2, 4, 8, 5, 6], 
[9, 6, 1, 5, 3, 7, 2, 8, 4], 
[2, 8, 7, 4, 1, 9, 6, 3, 5], 
[3, 4, 5, 2, 8, 6, 1, 7, 9]]
"""


def check_valid_values(vals: list) -> bool:
    found_values = set()
    for val in vals:
        if 0 <= val < len(list) + 1:
            if val != 0 and val in found_values:
                return False
            set.add(val)
        else:
            return False
    return True


def grid_validator(grid: list) -> bool:
    """
    Validates an input Sudoku grid
    """
    # Grid is None or blank
    # Non-integer value
    # Not a square

    valid_sudoku = True
    # Each element from 1-9 shoud exist in each row and column
    for row in grid:
        if not check_valid_values(row):
            return False
    for col_index in range(len(grid)):
        if not check_valid_values([grid[i][col_index] for i in range(len(grid))]):
            return False

    # if not (
    #         check_valid_values([item[i][j] for i in sub_mat_1 for j in sub_mat_1]) and
    #         check_valid_values(grid[0:3, 4:6]) and
    #         check_valid_values(grid[0:3, 6:9]) and
    #         check_valid_values(grid[3:5, 0:2]) and
    #         check_valid_values(grid[0:2, 0:2]) and
    #         check_valid_values(grid[0:2, 0:2]) and
    #         check_valid_values(grid[0:2, 0:2]) and
    #         check_valid_values(grid[0:2, 0:2]) and
    #         check_valid_values(grid[0:2, 0:2])
    # ):
    #     return False

    for i in grid[0: len(grid): 3]:
        for j in grid[0: len(grid): 3]:
            if not check_valid_values([grid[i + x][j + y] for x in range(3) for y in range(3)]):
                return False
    return True




