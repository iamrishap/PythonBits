"""
Given an index k, return the kth row of the Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
Example:
Input : k = 3
Return : [1,3,3,1]
NOTE : k is 0 based. k = 0, corresponds to the row [1].
Note:Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:

    def getRow(self, A):
        if A == 0:
            return [1]
        x = [1] * (A + 1)
        for i in range(1, A):
            x[i] = x[i - 1] * (A + 1 - i) // i
        return x


s = Solution()
print(s.getRow(5))
