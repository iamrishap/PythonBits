"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
N Queens: Example 1
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.'
both indicate a queen and an empty space respectively.
For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


# Unfortunately, there is no magic trick to solve this problem. This is more of a bruteforce problem.
# A more intelligent brute force.
# 1) There can exactly be one queen per row. Otherwise the 2 queens in the row would collide.
# If you miss out on a row, there cannot be N queens on the board.
# 2) Every column needs to have exactly one queen.
# 3) The left diagonal cannot have more than one queen ( Unique (row + col) )
# 4) The right diagonal cannot have more than one queen ( Unique (row - col) )


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        fin = []

        def solve(A, res):
            if len(res) == A:
                fin.append(res)
            for i in range(1, A + 1):
                if not self.attack(res, i):
                    solve(A, res + [i])

        solve(A, [])
        return [["." * (i - 1) + "Q" + "." * (A - i) for i in cols] for cols in fin]

    def attack(self, prev, pos):
        for i in range(len(prev)):
            if prev[i] == pos or abs(len(prev) - i) == abs(prev[i] - pos):
                return True
        return False


s = Solution()
print(s.solveNQueens(4))

# TODO: Check and understand the implementation later
