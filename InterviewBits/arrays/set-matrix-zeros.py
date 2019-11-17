"""
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.
Input Format:
The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.
Output Format:
Return a 2-d matrix that satisfies the given conditions.
Constraints:
1 <= N, M <= 1000
0 <= A[i][j] <= 1
Examples:
Input 1:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 1, 1]   ]
Output 1:
    [   [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1]   ]
Input 2:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]
Output 2:
    [   [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]   ]
"""


# Now, if R = 0, your job is simple. In the end, mark every element in the first row as 0.
# If R = 1, then leave the row as it is

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        col, row = set(), set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    row.add(i)
                    col.add(j)

        t = [0] * len(A[0])
        for r in row:
            A[r] = t

        for c in col:
            for i in range(len(A)):
                A[i][c] = 0

        return A

    class Solution:
        # @param A : list of list of integers
        # @return the same list modified
        def setZeroes(self, A):
            N = len(A)
            M = len(A[0])
            del_first_row = False
            del_first_col = False

            for i in range(N):
                if A[i][0] == 0:
                    del_first_row = True
                    break
            for i in range(M):
                if A[0][i] == 0:
                    del_first_col = True
                    break

            for i in range(N):
                for j in range(M):
                    if A[i][j] == 0:
                        A[i][0] = 2
                        A[0][j] = 2

            for i in range(1, N):
                for j in range(1, M):
                    if A[i][0] == 2:
                        A[i][j] = 0
                    elif A[0][j] == 2:
                        A[i][j] = 0
            for i in range(N):
                if A[i][0] > 1 or del_first_row:
                    A[i][0] = 0
            for i in range(M):
                if A[0][i] > 1 or del_first_col:
                    A[0][i] = 0

            return A
