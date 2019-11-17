"""
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.
The input corresponding to the above configuration :
["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.
 Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# Very simple simulation problem. Just need to keep track of the digits seen in every row,
# every column and every block as defined in the rules.
# Whenever you encounter a digit already seen, you know the sudoku is not valid.
# Note that this problem will get very complicated if you were to determine if the sudoku was solvable.

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        for i in range(9):
            if not self.isValidArray(list(A[i])) \
                    or not self.isValidArray([A[j][i] for j in range(9)]) \
                    or not self.isValidArray([A[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3] for j in range(9)]):
                return 0
        return 1

    def isValidArray(self, arr):
        s = set()
        for x in arr:
            if x in s:
                return False
            if x != '.':
                s.add(x)
        return True
