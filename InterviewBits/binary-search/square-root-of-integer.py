"""
Implement int sqrt(int x).
Compute and return the square root of x.
If x is not a perfect square, return floor(sqrt(x))
Example :
Input : 11
Output : 3
"""


# Think in terms of binary search.
# Let us say S is the answer.
# We know that 0 <= S <= x.
# Consider any random number r.
# If r*r <= x, S >= r
# If r*r > x, S < r.
# Maybe try to run a binary search for S

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        left = 0
        right = A
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= A:
                left = mid + 1
            else:
                right = mid - 1
        return right
