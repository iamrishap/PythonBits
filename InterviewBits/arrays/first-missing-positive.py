"""
Given an unsorted integer array, find the first missing positive integer.
Example:
Given [1,2,0] return 3,
[3,4,-1,1] return 2,
[-8, -7, -6] returns 1
Your algorithm should run in O(n) time and use constant space.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A = list(filter(lambda x: x > 0, A))
        # print(A)
        A = [len(A) + 2] + A  # Add the next number. This is for proper indexing (zero based).
        # print(A)
        for i, num in enumerate(A):
            num = abs(num)
            if num < len(A):
                A[num] = - abs(A[num])
        # print(A)
        for i in range(1, len(A)):
            if A[i] > 0:
                return i
        return len(A)


s = Solution()
s.firstMissingPositive([3, 5, 2, 1])
