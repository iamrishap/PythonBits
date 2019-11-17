"""
On a N * M chessboard, where rows are numbered from 1 to N and columns from 1 to M, there are queens at some cells.
Return a N * M array A, where A[i][j] is number of queens that can attack cell (i, j). While calculating answer for
cell (i, j), assume there is no queen at that cell.
Notes:
Queen is able to move any number of squares vertically, horizontally or diagonally on a chessboard. A queen cannot
jump over another queen to attack a position.
You are given an array of N strings, each of size M. Each character is either a 1 or 0 denoting if there is a queen at
that position or not, respectively.
Expected time complexity is worst case O(N*M).
For example,
Let chessboard be,
[0 1 0]
[1 0 0]
[0 0 1]
where a 1 denotes a queen at that position.
Cell (1, 1) is attacked by queens at (2, 1), (1,2) and (3,3).
Cell (1, 2) is attacked by queen at (2, 1). Note that while calculating this, we assume that there is no queen at (1, 2).
Cell (1, 3) is attacked by queens at (3, 3) and (1, 2).
and so on...
Finally, we return matrix
[3, 1, 2]
[1, 3, 3]
[2, 3, 0]
"""

# If you actually traverse in all 8 directions for each cell, total complexity in worst case will be O(N*M*(N+M)).
# Can you store some data for cells in such a way that for finding answer to cell (i, j)
# you just have to look at its neighbours only.
# We define f(i, j, k) as a number of queen attacks on the cell (i, j) from direction k.
# Eight directions can be given numbers 0 to 7.
# Now, to see how many attacks are there on a cell (i, j), we go to its neighbour in direction k(say n_i, n_j).
# If the cell (n_i, n_j) has a queen, then there is just 1 attack. Else, number of attacks is f(n_i, n_j, k).
# Can you formulate base cases?
# We just have to take the sum of f(i, j, k) for all k=0 to 7 to find the answer for the position (i, j).
# The total number of states is O(N*M*8) and the transition is O(1), so total complexity is O(N*M).

from collections import defaultdict


class Solution:
    # @param A : list of strings
    # @return a list of list of integers
    def queenAttack(self, A):
        n, m = len(A), len(A[0])
        res = [[0] * m for _ in range(n)]

        hasTop = [0] * m
        hasDiag = defaultdict(int)
        hasRdiag = defaultdict(int)
        for i in range(n):
            hasLeft = 0
            for j in range(m):
                res[i][j] += hasLeft + hasTop[j] + hasDiag[j - i] + hasRdiag[j + i]
                if A[i][j] == '1':
                    hasLeft = 1
                    hasTop[j] = 1
                    hasDiag[j - i] = 1
                    hasRdiag[j + i] = 1

        hasBottom = [0] * m
        hasDiag = defaultdict(int)
        hasRdiag = defaultdict(int)
        for i in range(n - 1, -1, -1):
            hasRight = 0
            for j in range(m - 1, -1, -1):
                res[i][j] += hasRight + hasBottom[j] + hasDiag[j - i] + hasRdiag[j + i]
                if A[i][j] == '1':
                    hasRight = 1
                    hasBottom[j] = 1
                    hasDiag[j - i] = 1
                    hasRdiag[j + i] = 1

        return res
