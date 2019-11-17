"""
Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle containing all ones and return its area.
Bonus if you can solve it in O(n^2) or less.
Example :
A : [  1 1 1
       0 1 1
       1 0 0
    ]
Output : 4
As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)
"""


# The bruteforce approach is to look at all pairs of (i,j) to (k,l) and check if its filled with 1s.
# This approach however is O(NNNNN^2) = O(N^6). [ N^4 ways to choose i,j,k,l and then N^2 elements in the square ].
# Can you optimize this approach if you had additional space to store results for your previous calculations ?
# Maybe if you knew the result for (i, j) to (k, l - 1) or (i, j) to (k - 1, l) or both ?
# We can improve from N^6 by storing in dp[i][j][k][l] if (i,j) to (k,l) is all filled with 1.
# dp[i][j[k][l] = 1 iff dp[i][j][k][l-1] = 1 && dp[i][j][k-1][l] = 1 and matrix[k][l] = 1.
# Now we can improve this further.
# What if with every (i,j) we stored the length of 1s in the same row i starting from (i,j).
# Can we move down in the column j from row i and determine the largest rectangle without having to visit all cells ?
# Lets max_x[i][j] denote the length of 1s in the same row i starting from (i,j).
# So our current max with one end of the rectangle at (i,j) would be max_x[i][j].
# As we move to the next row, there are 2 cases :
# 1) max_x[i+1][j] >= max_x[i][j] which means that we can take max_x[i][j] 1s from next column as well and extend
# our current rectangle as it is, with one more extra row.
# 11100000 - 111
# 11111100 - 111
# 2) max_x[i+1][j] < max_x[i][j] which means that if we want to extend our current rectangle to next row, we need
# to reduce the number of columns in it to max_x[i+1][j]
# 11100000 - 11
# 11000000 - 11
# As mentioned above, we keep increasing the columns and adjusting the width of the rectangle.
# O(N^3) time complexity.
# Even though N^3 is acceptable, it might be worth exploring a better solution.
# If you notice, laying out max_x[i][j] helps you make histograms in every row. Then the problem becomes of
# finding the maximum area in histograms ( which we have solved before in Stacks and Queues ) in O(n).
# This would lead to an O(N^2) solution. We strongly suggest you to explore the O(N^2) solution as well.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        for r in range(1, len(A)):
            for c in range(len(A[0])):
                if A[r][c] == 1:
                    A[r][c] += A[r - 1][c]
        best_ans = 0
        for hist in A:
            ans = self.solve_hist(hist)
            best_ans = max(ans, best_ans)
        return best_ans

    def solve_hist(self, hist):
        hist.append(0)
        stack = [(-1, -1)]
        best_ans = 0
        for r_op, val in enumerate(hist):
            while stack[-1][0] > val:
                v, i = stack.pop()
                l_op = stack[-1][1]
                l_cl = l_op + 1
                ans = v * (r_op - l_cl)
                best_ans = max(ans, best_ans)
            stack.append((val, r_op))
        return best_ans
