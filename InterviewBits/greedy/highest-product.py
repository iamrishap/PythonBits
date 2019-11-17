"""
Given an array A, of N integers A.
Return the highest product possible by multiplying 3 numbers from the array.
NOTE: Solution will fit in a 32-bit signed integer.
Input Format:
The first and the only argument is an integer array A.
Output Format:
Return the highest possible product.
Constraints:
1 <= N <= 5e5
Example:
Input 1:
A = [1, 2, 3, 4]
Output 1:
24
Explanation 1:
2 * 3 * 4 = 24
Input 2:
A = [0, -1, 3, 100, 70, 50]
Output 2:
350000
Explanation 2:
70 * 50 * 100 = 350000
"""


# Do we need to consider all the elements from the array ?
# Is it enough to consider just the 3 maximum numbers from the array ? Obviously No.
# Product of 2 negative numbers is positive. So, Negative numbers with higher absolute value might also be of interest.
# How about maximum 3 elements, and 2 negative elements with the highest absolute value ?
# Choosing 3 maximum elements in the array and 2 negative elements with the highest absolute value should be enough.
# There are various ways to calculate 3 maximum elements in the array ( and subsequently 2 negative elements with
# highest absolute value ). One such approach is maintaining 3 variables ( m1, m2, m3 where m1 > m2 > m3 ).
# When you encounter new value in the array, if the value is less than m3, then the variables are unaffected.
# Else, depending on where the new value lies, you can update the 3 values.
# Another approach could be maintaining a priority_queue of size 3. You pop out the smallest element if
# the new element if bigger than the smallest element, and then insert the new element into the priority queue.
# Once you have the 5 elements you desire,
# your answer would be one of the following :
# 1) Product of 3 maximum elements
# 2) Product of the 2 negative elements with max absolute value and maximum positive value.


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort(reverse=True)
        n = len(A) - 1
        if A[n] >= 0:
            p = A[0] * A[1] * A[2]
        elif A[0] > 0:
            p = max(A[0] * A[1] * A[2], A[0] * A[n] * A[n - 1])
        elif A[0] <= 0:
            p = A[0] * A[1] * A[2]
        return p
