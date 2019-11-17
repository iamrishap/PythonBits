"""
Given an array of positive elements, you have to flip the sign of some of its elements such that the resultant sum of
the elements of array should be minimum non-negative(as close to zero as possible). Return the minimum no. of elements
whose sign needs to be flipped such that the resultant sum is minimum non-negative.
Constraints:
 1 <= n <= 100
Sum of all the elements will not exceed 10,000.
Example:
A = [15, 10, 6]
ans = 1 (Here, we will flip the sign of 15 and the resultant sum will be 1 )
A = [14, 10, 4]
ans = 1 (Here, we will flip the sign of 14 and the resultant sum will be 0)
 Note that flipping the sign of 10 and 4 also gives the resultant sum 0 but flippings there are not minimum
"""


# Let the sum of all the given elements be S.
# This problem can be reduced to a Knapsack problem where we have to fill a Knapsack of capacity (S/2) as fully as
# possible and using the minimum no. of elements. We will fill the Knapsack with the given elements. Sign of all the
# elements which come into the knapsack will be flipped.
# As sum of all the elements in the Knapsack will be as close to S/2 as possible, we are indirectly calculating
# minimum non-negative sum of all the elements after flipping the sign. Give it a thought and code your way out!


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        n = len(A)

        def helper(i, cur, memo={}):
            """ Sub problem: minimum reachable from cur,
                by picking elements from A[i:]
                Return minimum reached, minimum numbers of flip """
            if i == n or cur == 0:
                return (cur, 0)
            if (i, cur) in memo:
                return memo[(i, cur)]
            res, flip = helper(i + 1, cur)  # Don't flip A[i]
            if 2 * A[i] <= cur:  # Flip A[i] if valid
                res2, flip2 = helper(i + 1, cur - 2 * A[i])
                res, flip = min((res, flip), (res2, flip2 + 1))
            memo[(i, cur)] = (res, flip)
            return res, flip

        return helper(0, sum(A))[1]
