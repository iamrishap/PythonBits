"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
 Note: You can only move either down or right at any point in time.
Example :
Input :
    [  1 3 2
       4 3 1
       5 6 1
    ]
Output : 8
     1 -> 3 -> 2 -> 1 -> 1
"""


#  Let DP[i][j] store the minimum sum of numbers along the path from top left to (i,j).
# Basically, DP[i][j] = A[i][j] + min(DP[i-1][j],DP[i][j-1]).
# You only need to figure out the base conditions and boundary conditions now.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        if (len(A) == 1):
            return sum(A[0])
        m = len(A)
        n = len(A[0])
        mat = [[0 for i in range(n)] for j in range(m)]
        mat[0][0] = A[0][0]
        for i in range(0, m):
            for j in range(0, n):
                if i > 0 and j > 0:
                    mat[i][j] = min(mat[i][j - 1], mat[i - 1][j]) + A[i][j]
                elif j == 0 and i > 0:
                    mat[i][j] = mat[i - 1][j] + A[i][j]
                elif i == 0 and j > 0:
                    mat[i][j] = mat[i][j - 1] + A[i][j]
        return mat[m - 1][n - 1]
