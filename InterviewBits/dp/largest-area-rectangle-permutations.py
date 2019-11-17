"""
Given a binary grid i.e. a 2D grid only consisting of 0’s and 1’s, find the area of the largest rectangle inside the
grid such that all the cells inside the chosen rectangle should have 1 in them. You are allowed to permutate the
columns matrix i.e. you can arrange each of the column in any order in the final grid.
Please follow the below example for more clarity.
Lets say we are given a binary grid of 3 * 3 size.
1 0 1
0 1 0
1 0 0
At present we can see that max rectangle satisfying the criteria mentioned in the problem is of 1 * 1 = 1 area
i.e either of the 4 cells which contain 1 in it. Now since we are allowed to permutate the columns of the given matrix,
we can take column 1 and column 3 and make them neighbours. One of the possible configuration of the grid can be:
1 1 0
0 0 1
1 0 0
Now In this grid, first column is column 1, second column is column 3 and third column is column 2 from the original
given grid. Now, we can see that if we calculate the max area rectangle, we get max area as 1 * 2 = 2 which is bigger
than the earlier case. Hence 2 will be the answer in this case.
"""


# Let’s try to think polynomial time approach.
# Let’s say for each index i.e. (i, j) pair, we store a value which corresponds to the number of consecutive cells
# having 1 as their value which are directly above that cell starting from the given cell itself. Lets store this
# value in an array called count. Thus count[i][j] will denote the number of
# consecutive 1’s starting from the cell (i, j) and continuing upwards.
# For example, for a given matrix
# 1 0 1
# 1 1 0
# 1 0 1
#  Its count matrix will be -
# 1 0 1
# 2 1 0
# 3 0 1
# Now, once we have got this array, let’s consider a row i. Each element of this row will have some count[i][j]
# value where j is from 1 to m. Now as permutation is allowed, we can select any order for keeping the columns.
# Let’s fix that ordering for time being with lower the value of count[i][j], the earlier it is getting placed.
# So we will have a sorted arrangement of columns according to their count[i][j] values. We can easily see that
# while traversing through the above sorted arrangement, we can calculate the maximum area possible for that particular
# row. On repeating this algorithm for each row of the grid will give us the maximum area rectangle
# possible in the given grid.

class Solution:
    def solve(self, A):
        x = len(A)
        y = len(A[0])
        for j in range(y):
            count = 0
            for i in range(x):  # Going column wise
                if A[i][j] == 1:
                    count = count + 1  # Number of 1s in row
                else:
                    count = 0  # If 0
                A[i][j] = count  # Setting Matrix entry with the count of 1s
        for k in range(x):
            A[k].sort(reverse=True)  # Descending order arrangement of 1s count
        size = 0
        for i in range(x - 1, -1, -1):
            for j in range(y - 1, -1, -1):
                mult1 = A[i][j]
                mult2 = j + 1  # This is non zero so all those to the left can be taken in the rectangle
                size = max(size, mult1 * mult2)  # Maximum Size by finding length*breadth
        return size  # Size denotes the Maximum Size of the rectangle with 1s


A = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 0, 1]
]

s = Solution()
print(s.solve(A))
