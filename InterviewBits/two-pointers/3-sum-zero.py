"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note:
 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2)
"""


# When the array is sorted, try to fix the least integer by looping over it.
# Let us say the least integer in the solution is arr[i].
# Now we need to find a pair of integers j and k such that :
#  arr[j] + arr[k] is -arr[i].
# To do that, let us try the 2 pointer approach.
# If we fix the two pointers at the end ( that is, i+1 and end of array ),
# we look at the sum.
# If the sum is smaller than 0, we increase the first pointer to increase the sum.
# If the sum is bigger than 0, we decrease the end pointer to reduce the sum.
# Getting a Time Limit exceeded or Output Limit exceeded?
# Make sure you handle case of empty input [].
# In C++/C, usually if you run a loop till array.size() - 2,
# it can lead to the program running indefinitely as array.size() is unsigned int,
# and the subtraction just makes it wrap over to a big integer.
# Make sure you are not processing the same triplets again.
# Skip over the duplicates in the array.
#  Try a input like :
# -1 -1 -1 -1 0 0 0 0 1 1 1 1
# Ideally, you should get only 2 pairs : {[-1 0 1], [0 0 0]}

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        if A.__len__() < 3:
            return []
        A.sort()
        ret = set()
        for index, ele_a in enumerate(A[:-2]):
            b = index + 1
            c = A.__len__() - 1
            while b < c:
                temp_sum = ele_a + A[b] + A[c]
                if temp_sum == 0:
                    ret.add((ele_a, A[b], A[c]))
                    b += 1
                    c -= 1
                elif temp_sum < 0:
                    b += 1
                else:
                    c -= 1
        return list(ret)
