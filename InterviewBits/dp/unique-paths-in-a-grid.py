"""
Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance,
if you are on (x,y), you can either go to (x, y + 1) or (x + 1, y).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Example :
There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
 Note: m and n will be at most 100.
"""


# Dynamic programming FTW.
# If you look at a cell, there are atmost 2 ways to reach it. From the cell left and up.
# If the cell does not have an obstacle, then the number of ways to reach this cell would be the summation of the
# number of ways to reach the immediate neighbors preceding it ( left and up ).

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        if not A: return 0
        if A[-1][-1] == 1 or A[0][0] == 1: return 0

        paths = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        paths[0][0] = 1

        for x in range(len(A)):
            for y in range(len(A[0])):
                prev_left_val = 0 if x - 1 < 0 else paths[x - 1][y]
                prev_down_val = 0 if y - 1 < 0 else paths[x][y - 1]
                paths[x][y] += (prev_left_val + prev_down_val) if A[x][y] == 0 else 0

        return paths[x][y]
