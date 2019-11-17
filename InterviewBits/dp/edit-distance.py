"""
Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character
Input Format:
The first argument of input contains a string, A.
The second argument of input contains a string, B.
Output Format:
Return an integer, representing the minimum number of steps required.
Constraints:
1 <= length(A), length(B) <= 450
Examples:
Input 1:
    A = "abad"
    B = "abac"
Output 1:
    1
Explanation 1:
    Operation 1: Replace d with c.
Input 2:
    A = "Anshuman"
    B = "Antihuman"
Output 2:
    2
Explanation 2:
    => Operation 1: Replace s with t.
    => Operation 2: Insert i.
"""


# int editDistance(string &S1, int index1, string &S2, int index2) {
# // BASE CASES
#
# if (S1[index1] == S2[index2]) {
#      return editDistance(S1, index1 + 1, S2, index2 + 1);
# } else {
#      return min(
#     1 + editDistance(S1, index1 + 1, S2, index2), // Delete S1 char
#             1 + editDistance(S1, index1, S2, index2 + 1), // Insert S2 char
#             1 + editDistance(S1, index1 + 1, S2, index2 + 1) // Replace S1 first char with S2 first char
#      );
# } }
# The above approach is definitely exponential.
# However, lets look at the number of ways in which the function can be called. S1 and S2 remain constant.
# The only thing changing is index1 and index2 which can take len(S1) * len(S2) number of values.
# Can you use it to memoize ?

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        n = len(A) + 1
        m = len(B) + 1
        M = [[0] * m for _ in range(n)]
        for j in range(m):
            M[0][j] = j  # Setting the boundary as number of characters
        for i in range(n):
            M[i][0] = i  # Setting the boundary as number of characters
        print(M)
        for i in range(1, n):
            for j in range(1, m):
                c = 0 if A[i - 1] == B[j - 1] else 1
                M[i][j] = min(M[i][j - 1] + 1, M[i - 1][j] + 1, M[i - 1][j - 1] + c)
        return M[-1][-1]


s = Solution()
print(s.minDistance('abad', 'abac'))
