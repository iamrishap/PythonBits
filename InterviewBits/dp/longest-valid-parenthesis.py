"""
Given a string A containing just the characters ’(‘ and ’)’.
Find the length of the longest valid (well-formed) parentheses substring.
Input Format:
The only argument given is string A.
Output Format:
Return the length of the longest valid (well-formed) parentheses substring.
Constraints:
1 <= length(A) <= 750000
For Example
Input 1:
    A = "(()"
Output 1:
    2
    Explanation 1:
        The longest valid parentheses substring is "()", which has length = 2.
Input 2:
    A = ")()())"
Output 2:
    4
    Explanation 2:
        The longest valid parentheses substring is "()()", which has length = 4.
"""


# Lets construct longest[i] where longest[i] denotes the longest set of parenthesis ending at index i.
#
# If s[i] is ‘(‘, set longest[i] to 0, because any string end with ‘(‘ cannot be a valid one.
# Else if s[i] is ‘)’
# If s[i-1] is ‘(‘, longest[i] = longest[i-2] + 2
# Else if s[i-1] is ‘)’ and s[i-longest[i-1]-1] == ‘(‘, longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]

class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        dpMap = dict()

        def dp(i):
            if i in dpMap:
                return dpMap[i]
            if i >= len(A) or A[i] == ')':
                return i - 1
            ans = i - 1
            if i + 1 < len(A):
                if A[i + 1] == ')':
                    ans = i + 1 + dp(i + 2) - (i + 2) + 1
                elif dp(i + 1) != i:
                    j = dp(i + 1) + 1
                    if j < len(A) and A[j] == ')':
                        ans = j + dp(j + 1) - (j + 1) + 1
            dpMap[i] = ans
            return ans

        return max(dp(i) - i + 1 for i in reversed(range(len(A))))
