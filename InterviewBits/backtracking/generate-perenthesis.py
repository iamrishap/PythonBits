"""
Generate all Parentheses II
Asked in:
Facebook
Microsoft
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses of length 2*n.
For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.
"""
class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, n):
        if n == 0:
            return ['']
        res = []
        for i in range(n):
            suffixs = self.generateParenthesis(i)
            res += [
                '(' + p + ')' + suffix for suffix in suffixs
                for p in self.generateParenthesis(n - i - 1)
            ]
        return sorted(res)


# TODO: Revisit to understand. Don't get it what's been done.
