"""
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
Note that even though we want you to return the new length, make sure to change the original array as well in place
Do not allocate extra space for another array, you must do this in place with constant memory.
 Example:
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
"""


# Notice that the array is sorted.
# This implies that all repetitions for an element are clustered together in the array.
# **Try maintaining 2 pointers in the array: **
# One pointer iterates over the array and
# Other pointer only moves per occurrence of a value in the array.
# Now you need to make sure we choose only one occurrence per
# cluster of repetition in the array, we could probably just check if A[i] != A[i+1].
# So, the second pointer only moves when A[i] != A[i+1]

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i, j = 1, 0
        while i < len(A):
            if A[i] != A[j]:
                A[j + 1] = A[i]
                j += 1

            i += 1
        del A[j + 1:]
        return len(A)
