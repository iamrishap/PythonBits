"""
Given two sequences A, B, count number of unique ways in sequence A,
to form a subsequence that is identical to the sequence B.
Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, “ACE” is a subsequence of “ABCDE” while “AEC” is not).
Input Format:
The first argument of input contains a string, A.
The second argument of input contains a string, B.
Output Format:
Return an integer representing the answer as described in the problem statement.
Constraints:
1 <= length(A), length(B) <= 700
Example :
Input 1:
    A = "abc"
    B = "abc"
Output 1:
    1
Explanation 1:
    Both the strings are equal.
Input 2:
    A = "rabbbit"
    B = "rabbit"
Output 2:
    3
Explanation 2:
    These are the possible removals of characters:
        => A = "ra_bbit"
        => A = "rab_bit"
        => A = "rabb_it"
    Note: "_" marks the removed character.
"""

# As a typical way to implement a dynamic programming algorithm, we construct a matrix dp,
# where each cell dp[i][j] represents the number of solutions of aligning substring T[0..i] with S[0..j];
# Rule 1). dp[0][j] = 1, since aligning T = “” with any substring of S would have only ONE solution
# which is to delete all characters in S.
# Rule 2). when i > 0, dp[i][j] can be derived by two cases:
# case 1). if T[i] != S[j], then the solution would be to ignore the character S[j] and
# align substring T[0..i] with S[0..(j-1)]. Therefore, dp[i][j] = dp[i][j-1].
# case 2). if T[i] == S[j], then first we could adopt the solution in case 1), but also we
# could match the characters T[i] and S[j] and align the rest of them (i.e. T[0..(i-1)] and S[0..(j-1)].
# As a result, dp[i][j] = dp[i][j-1] + d[i-1][j-1]
# e.g. T = B, S = ABC
# dp[1][2]=1: Align T’=B and S’=AB, only one solution, which is to remove character A in S’.


from functools import lru_cache


class Solution:
    # @param S : string
    # @param T : string
    # @return an integer
    def numDistinct(self, S, T):
        # dpMap = dict()

        @lru_cache(maxsize=None)
        def dp(i, j):
            # key = (i,j)
            # if key in dpMap:
            #     return dpMap[key]
            ans = 0
            if j == len(T) or i == len(S):
                ans = 1 if len(T) == j else 0
            else:
                ans = dp(i + 1, j)
                if S[i] == T[j]:
                    ans += dp(i + 1, j + 1)

            # dpMap[key] = ans
            return ans

        # Avoid recursion limit
        for i in reversed(range(len(S) + 1)):
            for j in reversed(range(min(i + 1, len(T) + 1))):
                dp(i, j)

        return dp(0, 0)

    def numDistinct_rec(self, A, B):
        d = {}

        def rec(p1, p2):
            if p2 > p1:  # What has to be made is greater than from what to make
                return 0
            elif p2 == -1:
                return 1
            if (p1, p2) not in d:
                if A[p1] == B[p2]:  # Try deleting one char from both A and B, deleting just one char from A
                    d[(p1, p2)] = rec(p1 - 1, p2 - 1) + rec(p1 - 1, p2)
                else:
                    d[(p1, p2)] = rec(p1 - 1, p2)  # Delete the last char from A
            return d[(p1, p2)]

        return rec(len(A) - 1, len(B) - 1)


s = Solution()
print(s.numDistinct())
print(s.numDistinct_rec())

# TODO: First solution is advanced. Didn't follow that one.
