"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).
You are given a target value to search. If found in the array, return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Input : [4 5 6 7 0 1 2] and target = 4
Output : 0
NOTE : Think about the case when there are duplicates.
Does your current solution work? How does the time complexity change?*
"""


# Think a modified version of the binary search.
# If the pivot is known, the binary search becomes trivial as the array to the either side of the pivot is sorted.
# Can you somehow search for the pivot in your binary search?
# First, we find the pivot (the index of minimum in the array).
# Once we know the pivot, to search for x,
# we can do a conventional binary search in the left and right part of the pivot in the array.
# Now, let us look at how binary search can be applied in this scenario to find the minimum.
# There are 2 cases:
# 1)
#           mid
#            |
#    6 7 8 9 1 2 3 4 5
# arr[mid] > arr[end]
# The min lies in (mid, end]
# Mid is excluded from the range because arr[mid] > arr[end]
# 2)
#          mid
#           |
#   6 7 8 9 1 2 3 4 5
# arr[mid] < arr[end]
# The min lies in [start, mid]
# 3) Note: If there are duplicates, making either decision might be difficult and hence linear search might be required.
#                mid
#                 |
# 1 1 1 1 2 0 1 1 1 1 1 1 1 1 1 1 1
# arr[mid] = arr[end]
#
# Indecisive. We would need to explore the whole array.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):

        lft, rgt = 0, len(A) - 1
        while lft <= rgt:
            mid = (lft + rgt) / 2
            l, m, r = A[lft], A[mid], A[rgt]
            if m == B:
                return mid
            elif l <= B < m or (l > m and not (m < B <= r)):
                # We choose left half if either :
                #    * left half is sorted and B in this range
                #    * left half is not sorted,
                #      but B isn't in the sorted right half.
                rgt = mid - 1
            else:
                lft = mid + 1

        return -1
