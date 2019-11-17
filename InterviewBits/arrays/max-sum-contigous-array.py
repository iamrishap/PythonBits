"""
Find the contiguous subarray within an array, A of length N which has the largest sum.
Input Format:
The first and the only argument contains an integer array, A.
Output Format:
Return an integer representing the maximum possible sum of the contiguous subarray.
Constraints:
1 <= N <= 1e6
-1000 <= A[i] <= 1000
For example:
Input 1:
    A = [1, 2, 3, 4, -10]
Output 1:
    10
Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.
Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output 2:
    6
Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.
"""


inf = float('inf')
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        max_so_far, max_sum = 0, -inf
        for val in A:
            max_so_far += val
            max_sum = max(max_so_far, max_sum)
            # Doing this last, to handle case
            # when all numbers are negative.
            max_so_far = max(max_so_far, 0)
        return max_sum


s = Solution()
print(s.maxSubArray([1, 2, 3, 4, -10]))
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
