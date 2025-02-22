"""
Given an array of integers, A of length N, find length of longest subsequence which is first increasing then decreasing.
Input Format:
The first and the only argument contains an integer array, A.
Output Format:
Return an integer representing the answer as described in the problem statement.
Constraints:
1 <= N <= 3000
1 <= A[i] <= 1e7
Example:
Input 1:
    A = [1, 2, 1]
Output 1:
    3
Explanation 1:
    [1, 2, 1] is the longest subsequence.
Input 2:
    [1, 11, 2, 10, 4, 5, 2, 1]
Output 2:
    6
Explanation 2:
    [1 2 10 4 2 1] is the longest subsequence.
"""

# Construct array inc[i] where inc[i] stores Longest Increasing subsequence ending with A[i]. O(n^2) DP.
# Construct array dec[i] where dec[i] stores Longest Decreasing subsequence ending with A[i]. O(n^2) DP.
# Now we need to find the maximum value of (inc[i] + dec[i] - 1)

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        n = len(A)
        inc = [1] * n
        for i in range(1, n):
            for j in range(0, i):  # Just an inner loop to consider items less than i loop
                if A[i] > A[j] and inc[j] + 1 > inc[i]:
                    inc[i] = inc[j] + 1
        dec = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if A[i] > A[j] and dec[j] + 1 > dec[i]:
                    dec[i] = dec[j] + 1
        maximum = 1
        for x, y in zip(inc, dec):  # Iterating two arrays together
            maximum = max(maximum, x + y)
        return maximum - 1


s = Solution()
print(s.longestSubsequenceLength([1, 11, 2, 10, 4, 5, 2, 1]))
