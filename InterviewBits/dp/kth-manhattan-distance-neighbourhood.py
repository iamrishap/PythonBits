"""
Given a matrix M of size nxm and an integer K, find the maximum element in the K
manhattan distance neighbourhood for all elements in nxm matrix.
In other words, for every element M[i][j] find the maximum element M[p][q] such that abs(i-p)+abs(j-q) <= K.
Note: Expected time complexity is O(N*N*K)
Constraints:
1 <= n <= 300
1 <= m <= 300
1 <= K <= 300
0 <= M[i][j] <= 1000
Example
Input:
M  = [[1,2,4],[4,5,8]] , K = 2
Output:
ans = [[5,8,8],[8,8,8]]
"""


# This problem can be solved easily using dynamic programming.
# DP recurrence:
# dp[k][i][j] = ans. for kth manhattan distance for element (i,j)
# dp[k+1][i][j] = max(dp[k][i-1][j], dp[k][i+1][j], dp[k][i][j-1], dp[k][i][j+1], dp[k][i][j] )
# Recurrence is easy to get once you draw the figure.

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, B, A):
        r, c = len(A), len(A[0])
        M = [[A[i][j] for j in range(c)] for i in range(r)]
        M_ = [[A[i][j] for j in range(c)] for i in range(r)]
        for k in range(B):
            for i in range(r):
                for j in range(c):
                    M_[i][j] = max(M[i][j], M[i - 1][j] if i > 0 else 0, M[i + 1][j] if i < r - 1 else 0,
                                   M[i][j - 1] if j > 0 else 0, M[i][j + 1] if j < c - 1 else 0)
            M_, M = M, M_
        return M
