"""
Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers
is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.
Note: You can choose more than 2 numbers.
Input Format:
The first and the only argument of input contains a 2d matrix, A.
Output Format:
Return an integer, representing the maximum possible sum.
Constraints:
1 <= N <= 20000
1 <= A[i] <= 2000
Example:
Input 1:
    A = [   [1]
            [2]    ]
Output 1:
    2
Explanation 1:
    We will choose 2.
Input 2:
    A = [   [1, 2, 3, 4]
            [2, 3, 4, 5]    ]
Output 2:
    We will choose 3 and 5.
"""


# Suppose we have 2 * N list :
# 1 |  2  |  3  | 4
# 2 |  3  |  4  | 5
# Now suppose we choose 2, then we can't choose the element just above it 1,
# the element next it 3, or the element diagonally opposite.
# In other words, if we are on (x, y), then if we choose (x, y), we can't choose
# (x + 1, y), (x, y + 1) and (x + 1, y + 1)

# This means that choosing V[0][i] or V[1][i] has identical bearing on the elements which are ruled out.
# So, instead we replace each column with a single element which is the max of V[0][i], V[1][i]
# Now we have the list as : 2 3 4 5
# Now our recurrence relation will depend only on position i and,
# a "include_current_element" which will denote whether we picked last element or not.


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        if len(A[0]) == 1:
            return max(A[0][-1], A[1][-1])
        n = len(A[0])
        arr = [0 for i in range(n)]
        arr[-1] = max(A[0][-1], A[1][-1])  # Choosing the max of the last elements
        arr[-2] = max(A[0][-2], A[1][-2], arr[-1])  # Either choosing the second last column or last column max
        for i in range(n - 3, -1, -1):
            temp = max(A[0][i], A[1][i])  # Instead of changing/creating array, just store the present value
            arr[i] = max(temp + arr[i + 2], arr[i + 1])
        return arr[0]
