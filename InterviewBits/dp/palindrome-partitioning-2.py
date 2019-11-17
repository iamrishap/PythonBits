"""
Given a string A, partition A such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of A.
Input Format:
The first and the only argument contains the string A.
Output Format:
Return an integer, representing the answer as described in the problem statement.
Constraints:
1 <= length(A) <= 501
Examples:
Input 1:
    A = "aba"
Output 1:
    0
Explanation 1:
    "aba" is already a palindrome, so no cuts are needed.
Input 2:
    A = "aab"
Output 2:
    1
Explanation 2:
    Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


# Firstly, we should be able to answer if substring [i,i+1,….j]
# is palindrome or not in O(1) with pre-computation of O(n^2).
# Now try to come up with some DP state which can find minimum cut using above data.

class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        def palin(string):
            if string == string[::-1]:
                return 1
            else:
                return 0

        dp = [0 for i in range(len(A) + 1)]
        dp[-1] = -1
        for i in range(len(A) - 1, -1, -1):
            val = len(A) - 1 - i
            for j in range(i + 1, len(A) + 1):
                if palin(A[i:j]) == 1:
                    val = min(val, 1 + dp[j])
            dp[i] = val
        return dp[0]
