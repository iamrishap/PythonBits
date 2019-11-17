"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
Return an integer corresponding to the maximum product possible.
Example :
Input : [2, 3, -2, 4]
Return : 6
Possible with [2, 3]
"""

# If there were no zeros or negative numbers, then the answer would definitely be the product of the whole array.
# Now lets assume there were no negative numbers and just positive numbers and 0. In that case we could maintain a
# current maximum product which would be reset to A[i] when 0s were encountered.
# When the negative numbers are introduced, the situation changes ever so slightly. We need to now maintain the
# maximum product in positive and maximum product in negative. On encountering a negative number, the maximum product
# in negative can quickly come into picture.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        assert len(A) > 0
        ans = A[0]
        ma, mi = 1, 1
        for a in A:
            ma, mi = max(a, a*ma, a*mi), min(a, a*ma, a*mi)
            ans = max(ans, ma, mi)
        return ans
