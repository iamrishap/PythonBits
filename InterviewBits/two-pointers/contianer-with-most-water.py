"""
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Your program should return an integer which corresponds to the maximum area of water that can be contained
( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane
we are working with for simplicity ).
 Note: You may not slant the container.
Example :
Input : [1, 5, 4, 3]
Output : 6
Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3.
So total area = 3 * 2 = 6
"""


# Area will be basically min(ai,aj)*(j-i) where j>i.
# Approach 1 (in direction of O(n)) :
# Will the area be maximum if you take j-i to be maximum. If not, then can you reduce the problem to simpler set?
# Approach 2 (in direction of O(nlogn)) :
# Sort the elements with their indexes in descending order. Start iterating from first position of sorted array
# while maintaing the maximum of answer. How?
# Description of approach 1:
# Note 1: When you consider a1 and aN, then the area is (N-1) * min(a1, aN).
# Note 2: The base (N-1) is the maximum possible.
# This implies that if there was a better solution possible, it will definitely have height greater than min(a1, aN).
# B * H > (N-1) * min(a1, aN)
# We know that, B < (N-1)
# So, H > min(a1, aN)
# This means that we can discard min(a1, aN) from our set and look to solve this problem again from the start.
# If a1 < aN, then the problem reduces to solving the same thing for a2, aN.
# Else, it reduces to solving the same thing for a1, aN-1


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        ans = 0
        n = len(A)
        i, j = 0, n - 1
        while i < j:
            ans = max(ans, min(A[i], A[j]) * (j - i))
            if A[i] < A[j]:
                i += 1
            else:
                j -= 1
        return ans
