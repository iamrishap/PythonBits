"""
Find the largest continuous sequence in a array which sums to zero.
Example:
Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}
 NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.
"""


# Lets try to reduce the problem to a much simpler problem.
# Lets say we have another array sum where
#   sum[i] = Sum of all elements from A[0] to A[i]
# Note that in this array, sum of elements from A[i] to A[j] = Sum[j] - Sum[i-1]
# We need to find j and i such that sum of elements from A[i] to A[j] = 0
#  Or Sum[j] - Sum[i-1] = 0
#  Or Sum[j] = Sum[i-1]
# Now, the problem reduces to finding 2 indices i and j such that sum[i] = sum[j]
# How can you solve the above problem ?
# There are two steps:
# 1. Create cumulative sum array where ith index in this array represents total sum from 1 to ith index element.
# 2. Iterate all elements of cumulative sum array and use hashing to find two elements
# where value at ith index == value at jth index but i != j.
# 3. IF element is not present in hash in fill hash table with current element.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        sumDict = {0: -1}
        total = 0
        maxLCS, maxi, maxj = 0, -1, -1

        for i, val in enumerate(A):
            total += val
            if total in sumDict:
                if maxLCS < i - sumDict[total]:
                    maxLCS = i - sumDict[total]
                    maxi = sumDict[total] + 1
                    maxj = i
            else:
                sumDict[total] = i
        return A[maxi: maxj + 1] if maxLCS else []
