"""
You are given an array of N integers, A1, A2 ,…, AN and an integer K.
Return the of count of distinct numbers in all windows of size K.
Formally, return an array of size N-K+1 where i’th element in this array contains
number of distinct elements in sequence Ai, Ai+1 ,…, Ai+k-1.
Note:
 If K > N, return empty array.
 A[i] is a signed integer
For example,
A=[1, 2, 1, 3, 4, 3] and K = 3
All windows of size K are
[1, 2, 1]
[2, 1, 3]
[1, 3, 4]
[3, 4, 3]
So, we return an array [2, 3, 3, 2].
"""


# If you have solution for window [i, i+k-1], can you quickly build solution for window [i+1, i+k]?
# If we have a data structure where we can maintain count of all keys and number of distinct keys,
# then we just have to reduce count of key A[i] and increasing count of A[i+k].
# If count of some key has been reduced to zero, we need to remove that key.
# This structure is a hashmap. All operations that we have said a constant time in it.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        app = {}
        ans = []
        for x in range(B):
            if A[x] not in app:
                app[A[x]] = 1
            else:
                app[A[x]] += 1
        ans.append(len((app)))
        for x in range(B, len(A)):
            if A[x] in app:
                app[A[x]] += 1
            else:
                app[A[x]] = 1
            if app[A[x - B]] == 1:
                del app[A[x - B]]
            else:
                app[A[x - B]] -= 1
            ans.append(len(app))
        return ans
