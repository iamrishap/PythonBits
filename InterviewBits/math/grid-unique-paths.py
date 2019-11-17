"""
A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).
Path Sum: Example 1
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).
How many possible unique paths are there?
Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.
Example :
Input : A = 2, B = 2
Output : 2
2 possible routes : (0, 0) -> (0, 1) -> (1, 1)
              OR  : (0, 0) -> (1, 0) -> (1, 1)
"""

# Note that you have to take m + n - 2 steps in total. You have to take (m - 1)
# steps going down and (n-1) steps going right. Can you relate this to combinatorics?
# Let 0 denote a down step and 1 denote a right step.
# So we need to find out the number of strings of length m + n - 2 which have exactly m - 1 zeroes and n - 1 ones.
# Essentially we need to choose the positions of ‘1s’, and then ‘0s’ fall into the remaining positions.
# So, the answer becomes Choose(m+n-2, n - 1).

from math import factorial


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        return int(factorial(A + B - 2) / (factorial(A - 1) * factorial(B - 1)))

    def uniquePath_dp(self, A, B):
        numPaths = [[1 for j in range(B)] for i in range(A)]
        for i in range(1, A):
            for j in range(1, B):
                numPaths[i][j] = numPaths[i - 1][j] + numPaths[i][j - 1]
        return numPaths[-1][-1]
