"""
Find the longest increasing subsequence of a given array of integers, A.
In other words, find a subsequence of array in which the subsequence’s elements are
in strictly increasing order, and in which the subsequence is as long as possible.
This subsequence is not necessarily contiguous, or unique.
In this case, we only care about the length of the longest increasing subsequence.
Input Format:
The first and the only argument is an integer array A.
Output Format:
Return an integer representing the length of the longest increasing subsequence.
Constraints:
1 <= length(A) <= 2500
1 <= A[i] <= 2000
Example :
Input 1:
    A = [1, 2, 1, 5]
Output 1:
    3
Explanation 1:
    The sequence : [1, 2, 5]
Input 2:
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output 2:
    6
Explanation 2:
    The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer

    def lis(self, A):
        if len(A) == 0:
            return 0
        arr = [1] * len(A)  # array to store the count of subsequences
        # iterate over the complete array
        for i in range(1, len(A)):
            # check the previous largest subsequence before this element
            # and update the current element value
            for j in range(i - 1, -1, -1):
                if A[i] > A[j]:
                    arr[i] = max(arr[i], arr[j] + 1)
        return max(arr)


arr = [1, 11, 2, 10, 4, 5, 2, 1]
s = Solution()
print("Length of lis is", s.lis(arr))
