"""
Given an array of integers A. There is a sliding window of size B which
is moving from the very left of the array to the very right.
You can only see the w numbers in the window. Each time the sliding window moves
rightwards by one position. You have to find the maximum for each window.
The following example will give you more clarity.
The array A is [1 3 -1 -3 5 3 6 7], and B is 3.
Window position	        Max
———————————-	        ————————-
[1 3 -1] -3 5 3 6 7	    3
1 [3 -1 -3] 5 3 6 7	    3
1 3 [-1 -3 5] 3 6 7	    5
1 3 -1 [-3 5 3] 6 7	    5
1 3 -1 -3 [5 3 6] 7	    6
1 3 -1 -3 5 [3 6 7]	    7
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].
Note: If B > length of the array, return 1 element with the max of the array.
Input Format
The first argument given is the integer array A.
The second argument given is the integer B.
Output Format
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1]
For Example
Input 1:
    A = [1, 3, -1, -3, 5, 3, 6, 7]
    B = 3
Output 1:
    C = [3, 3, 5, 5, 6, 7]
"""


# Approach 1 :
# The obvious brute force solution with run time complexity of O(nw) is definitely not efficient enough.
# Every time the window is moved, you have to search for a total of w elements in the window.
# Approach 2:
# A heap data structure quickly comes to mind. We could boost the run time to approximately O(n lg w)
# (Note that I said approximately because the size of the heap changes constantly and averages about w).
# Insert operation takes O(lg w) time, where w is the size of the heap. However, getting the maximum value is cheap,
# it merely takes constant time as the maximum value is always kept in the root (head) of the heap.
# As the window slides to the right, some elements in the heap might not be valid anymore (range is outside of
# the current window). How should you remove them? You would need to be somewhat careful here. Since you only
# remove elements that are out of the window’s range, you would need to keep track of the elements’ indices too.
# TIme complexity : O ( n log n ). Not good enough.
# Approach 3 :
# A double-ended queue should do the trick here.
# The double-ended queue is the perfect data structure for this problem. It supports insertion/deletion from the front
# and back. The trick is to find a way such that the largest element in the window would always appear in the front of
# the queue. How would you maintain this requirement as you push and pop elements in and out of the queue?
# You might notice that there are some redundant elements in the queue that we shouldn’t even consider about.
# For example, if the current queue has the elements: [10 5 3], and a new element in the window has the element 11.
# Now, we could have emptied the queue without considering elements 10, 5, and 3, and insert only element 11
# into the queue. A natural way most people would think is to try to maintain the queue size the same as the window’s
# size. Try to break away from this thought and try to think outside of the box. Removing redundant elements and
# storing only elements that need to be considered in the queue is the key to achieve the efficient O(n) solution.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        if B >= len(A):
            return [max(A)]

        result = [0] * (len(A) - B + 1)
        deque = []

        for i in range(len(A)):
            if deque and deque[0] == i - B:
                del deque[0]
            while deque and A[deque[-1]] < A[i]:
                del deque[-1]
            deque.append(i)
            if i + 1 >= B:
                result[i - B + 1] = A[deque[0]]

        return result
