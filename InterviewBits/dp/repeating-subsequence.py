"""
Given a string A, find if there is any subsequence that repeats itself.
A subsequence of a string is defined as a sequence of characters generated by deleting
some characters in the string without changing the order of the remaining characters.
NOTE : sub-sequence length should be greater than or equal to 2.
Input Format:
The first and the only argument of input contains a string A.
Output Format:
Return an integer, 0 or 1:
    => 0 : False
    => 1 : True
Constraints:
1 <= length(A) <= 100
Examples:
Input 1:
    A = "abab"
Output 1:
    1
Explanation 1:
    "ab" is repeated.
Input 2:
    A = "abba"
Output 2:
    0
Explanation 2:
    There is no repeating subsequence.
"""


# Now, to find longest repeating subsequence, lets try finding the longest common subsequence
# between the string A and itself ( LCS(A, A) ). The only restriction we want to impose is that you cannot match a
# character with its replica in the other string. In other words, if S1 and S2 are the replicas of the string
# for which we want to find LCS, S1[i] != S2[i] for all index i.
# Rec(i, j) =   |
#               |   Rec(i + 1, j)
#          max  |
#               |   Rec(i, j + 1)
#               |
#               |   Rec(i + 1, j + 1) + 1 IF i != j and A[i] == A[j]


class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        # tab represents length of matching substring from index i to j
        tab = [[0 for i in range(len(A) + 1)] for j in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(A) + 1):
                if i != j and A[i - 1] == A[j - 1]:
                    tab[i][j] = 1 + tab[i - 1][j - 1]  # For i and j value increments due to match
                    if tab[i][j] >= 2:
                        return 1
                else:
                    tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])
        return 0


A = 'abcdbcab'
s = Solution()
print(s.anytwo(A))
