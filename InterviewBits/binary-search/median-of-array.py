"""
There are two sorted arrays A and B of size m and n respectively.
Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).
The overall run time complexity should be O(log (m+n)).
Sample Input
A : [1 4 5]
B : [2 3]
Sample Output
3
 NOTE: IF the number of elements in the merged array is even,
 then the median is the average of n / 2 th and n/2 + 1th element.
For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5
"""


# Given a sorted array A of length m, we can split it into two parts:
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# All the elements in right part are greater than the elements in left part.
# The left part has “i” elements, and right part has “m - i” elements.
# There are “m + 1” kinds of splits. (i = 0 ~ m)
# When i = 0, the left part has “0” elements, right part has “m” elements.
# When i = m, the left part has “m” elements, right part has “0” elements.
# For array B, we can split it with the same way:
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# The left part has “j” elements, and right part has “n - j” elements.
# Put A’s left part and B’s left part into one set. (Let us name this set “LeftPart”)
# Put A’s right part and B’s right part into one set. (Let us name this set”RightPart”)
#         LeftPart           |            RightPart
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# If we can ensure the following:
# 1) LeftPart’s length == RightPart’s length (or RightPart’s length + 1)
# 2) All elements in RightPart is greater than elements in LeftPart,
# then we split all elements in {A, B} into two parts with eqaul length, and one part is
# always greater than the other part.
# Then the median can be easily found.
# The expected time complexity gives away binary search in this case.
# We are going to do binary search for the answer in this case.
# Given a sorted array A of length m, we can split it into two parts:
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# All elements in right part are greater than elements in the left part.
# The left part has i elements, and right part has m - i elements.
# There are m + 1 kinds of splits.
# (i = 0 ~ m)
# When i = 0, the left part has “0” elements, the right part has “m” elements.
# When i = m, the left part has “m” elements, right part has “0” elements.
# For the array B, we can split it in the same way:
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# The left part has “j” elements, and right part has “n - j” elements.
# Put A’s left part and B’s left part into one set. (Let’s name this set “LeftPart”)
# Put A’s right part and B’s right part into one set. (Let’s name this set”RightPart”)
#         LeftPart           |            RightPart
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# If we can ensure the following:
# LeftPart’s length == RightPart’s length (or RightPart’s length + 1)
# All elements in RightPart is greater than elements in LeftPart,
# then we can split all elements in {A, B} into two parts with equal length, and one part is always greater than the other part.
# Then the median can thus be easily found.
# To ensure these two condition, we just need to ensure:
# Condition 1 :
#  i + j == (m - i) + (n - j)
#  OR i + j == (m - i) + (n - j) + 1
# Which means if n >= m,
# i = 0 to m
# j = (m + n + 1) / 2 - i
# Condition 2
#  B[j - 1] <= A[i] and A[i - 1] <= B[j]
# Considering edge values, we need to ensure:
#    (j == 0 or i == m or B[j - 1] <= A[i]) and
#    (i == 0 or j == n or A[i - 1] <= B[j])
# So, all we need to do is:
# Search i from 0 to m, to find an object i to meet condition (1) and (2) above.
# And we can do this search by binary search.
# How?
# If B[j0 - 1] > A[i0], than the object ix can’t be in [0, i0].
# Why?
# Because if
#   ix < i0,
#   => jx = (m + n + 1) / 2 - ix > j0
#   => B[jx - 1] >= B[j0 - 1] > A[i0] >= A[ix].
# This violates the condition (2). So ix can’t be less than i0.
#
# And if A[i0 - 1] > B[j0], than the object ix can’t be in [i0, m].
# So we can do the binary search following the steps described below:
#
# set imin, imax = 0, m, then start searching in [imin, imax]
# Search in [imin, imax]:
#     i = (imin + imax) / 2
#     j = ((m + n + 1) / 2) - i
#     if B[j - 1] > A[i]:
#         search in [i + 1, imax]
#     else if A[i - 1] > B[j]:
#         search in [imin, i - 1]
#     else:
#         if m + n is odd:
#             answer is max(A[i - 1], B[j - 1])
#         else:
#             answer is (max(A[i - 1], B[j - 1]) + min(A[i], B[j])) / 2


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


# TODO: Left as it is tricky.
