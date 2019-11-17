"""
Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
Note that even though we want you to return the new length, make sure to change the original array as well in place
For example,
Given input array A = [1,1,1,2],
Your function should return length = 3, and A is now [1,1,2].
"""


# Notice that the array is sorted. This implies that all repetitions for an element are clustered together in the array.
# Try maintaining 2 pointers in the array:
# One pointer iterates over the array
# Other pointer only moves per occurrence of a value in the array.
# Now you need to make sure we choose atmost 2 occurrences per cluster of repetition in the array,
# We could probably just check **if A[i] != A[i+1] || A[i] != A[i+2] **
# So, the second pointer only moves when A[i] != A[i+1] || A[i] != A[i+2]

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 2
        fp = 2
        while i < len(A):
            if A[fp - 1] != A[i] or A[fp - 2] != A[i]:
                A[fp] = A[i]
                fp += 1
            i += 1
        return fp
