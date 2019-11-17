"""
Two kingdoms are on a war, kingdom X and kingdom Y. As a war specialist of kingdom X, you scouted kingdom Y area.
A kingdom area is defined as a N x M grid with each cell denoting a village.
Each cell has a value which denotes the strength of each corresponding village.
The strength can also be negative, representing those warriors of your kingdom who were held hostages.
There’s also another thing to be noticed.
The strength of any village on row larger than one (2<=r<=N) is stronger or equal
to the strength of village which is exactly above it.
The strength of any village on column larger than one (2<=c<=M) is stronger or equal to the
strength of vilage which is exactly to its left.
(stronger means having higher value as defined above).
So your task is, find the largest sum of strength that you can erase by bombing one sub-matrix in the grid.
Input format:
First line consists of 2 integers N and M denoting the number of rows and columns in the grid respectively.
The next N lines, consists of M integers each denoting the strength of each cell.
1 <= N <= 1500
1 <= M <= 1500
-200 <= Cell Strength <= 200
Output:
The largest sum of strength that you can get by choosing one sub-matrix.
Example:
Input:
3 3
-5 -4 -1
-3 2 4
2 5 8
Output:
19
Explanation:
Bomb the sub-matrix from (2,2) to (3,3): 2 + 4 + 5 + 8 = 19
"""


# Based on the observation in Hint 1, we can assume that the largest sub-array strength may start from any point,
# but will definitely end on bottom-right cell (N,M).
# Therefore, we can use dynamic programming to find the sum of sub-matrix starting
# from the bottom-right cell (N,M) going up and left.
# DP[i][j] = DP[i+1][j] + DP[i][j+1] - DP[i+1][j+1]
# Find the maximum answer from DP[i][j] for each (i,j)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        if n < 1 or m < 1:
            return 0
        reversedprefix_arr = []
        for arr in A:
            prefix_arr_cur = [0] * m
            prefix_arr_cur[m - 1] = arr[m - 1]
            for j in range(m - 2, -1, -1):
                prefix_arr_cur[j] = prefix_arr_cur[j + 1] + arr[j]
            reversedprefix_arr.append(prefix_arr_cur)
        arr = [0] * m
        max_sum = A[-1][-1]
        for i in range(n - 1, -1, -1):
            arr = [x + y for x, y in zip(arr, reversedprefix_arr[i])]
            max_sum = max(max_sum, max(arr))
        return max_sum
