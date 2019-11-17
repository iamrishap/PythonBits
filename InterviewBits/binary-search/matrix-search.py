"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example:
Consider the following matrix:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true )
Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem
"""


# If you write down the numbers of row 1 followed by numbers in row2,
# row3 and so on, do you think the resulting array would be sorted ?
# If yes, how do you search for a number efficiently in a sorted array ?

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        m = len(A)
        n = len(A[0])
        start = 0
        end = m * n - 1

        while start <= end:
            mid = (start + end) // 2
            i = mid // n
            j = mid % n
            if B == A[i][j]:
                return 1
            elif B > A[i][j]:
                start = mid + 1
            else:
                end = mid - 1
        return 0


# TODO: Left for later.
