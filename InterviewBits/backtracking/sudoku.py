"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'
You may assume that there will be only one unique solution.
A sudoku puzzle, and its solution numbers marked in red.
Example :
For the above given diagrams, the corresponding input to your program will be
[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
and we would expect your program to modify the above array of array of characters to
[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]
"""


class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        def findempty(grid, row, col):
            # row=0
            col = 0
            for row in range(row, 9):
                for col in range(9):
                    if grid[row][col] == 0:
                        return row, col, True
            return row, col, False

            # CHECK THE 3*3 SMALL GRID

        def checkSmallBox(grid, row, col, num):
            j = col - (col % 3)
            i = row - (row % 3)
            x = i
            y = j
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if grid[x][y] == num:
                        return False
            return True

        # CHECK HORIZONTAL AND VERTICAL
        def checkXY(grid, row, col, num):
            # HORIZONTAL
            for x in range(9):
                if grid[row][x] == num:
                    return False
            # VERTICAL
            for x in range(9):
                if grid[x][col] == num:
                    return False
            return True

        def Sudoku(grid, row, col):
            arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            k = 0

            # CHECK WHETHER THERE IS ANY BLANK BOX
            row, col, result = findempty(grid, row, col)
            if result == False:
                return True, grid

            for k in range(1, 10):
                if checkSmallBox(grid, row, col, k):
                    if checkXY(grid, row, col, k):
                        grid[row][col] = k
                        res, gri = Sudoku(grid, row, col)
                        if res:
                            return True, grid
                        grid[row][col] = 0

            return False, grid

        for i in range(9):
            A[i] = [int(A[i][elem].replace(".", "0")) for elem in range(9)]

        bl, A = Sudoku(A, 0, 0)

        for i in range(9):
            A[i] = "".join(list(map(str, A[i])))

        return A


# TODO: Revisit to understand. I just skipped it this time.
