"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input Format:
First and only argument is a N x M character matrix A
Output Format:
make changes to the the input only as matrix is passed by reference.
Constraints:

    1 <= N,M <= 1000
For Example:

Input 1:
    A = [ [X, X, X, X],
          [X, O, O, X],
          [X, X, O, X],
          [X, O, X, X] ]
Output 1:
    After running your function, the board should be:
    A = [ [X, X, X, X],
          [X, X, X, X],
          [X, X, X, X],
          [X, O, X, X] ]
Explanation:
O in (4,2) is not surrounded by X from below.
"""


class Solution:
    def solve(self, A):

        M = len(A)
        N = len(A[0])

        def inbounds(i, j):
            if i >= 0 and i < M and j >= 0 and j < N:
                return True
            return False

        def mark(i, j):
            todo = [(i, j)]
            while todo:
                i, j = todo.pop()
                if inbounds(i, j) and A[i][j] == 'O' and marked[i][j] == 0:
                    marked[i][j] = 1
                    todo.append((i + 1, j))
                    todo.append((i - 1, j))
                    todo.append((i, j + 1))
                    todo.append((i, j - 1))

        marked = [[0 for _ in range(N)] for _ in range(M)]
        # We already know chunks of O which remain as O are the ones
        # which have at least one O connected to them which is on the boundary.
        # Use BFS starting from ‘O’s on the boundary and mark them as ‘B’ (or 1),
        # then iterate over the whole board and mark ‘O’ as ‘X’ and ‘B’ (or 1) as ‘O’.
        for i in range(M):
            mark(i, 0)
            mark(i, N - 1)
        for j in range(N):
            mark(0, j)
            mark(M - 1, j)

        for i in range(1, M - 1):
            for j in range(1, N - 1):
                if A[i][j] == 'O' and marked[i][j] == 0:
                    A[i][j] = 'X'
        return A


A = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

A = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

A = [
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'O', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X', 'X']
]
s = Solution()
print(s.solve(A))
