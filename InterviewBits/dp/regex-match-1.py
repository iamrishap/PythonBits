"""
Implement wildcard pattern matching with support for ‘?’ and ‘*’ for strings A and B.
’?’ : Matches any single character.
‘*’ : Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
Input Format:
The first argument of input contains a string A.
The second argument of input contains a string B.
Output Format:
Return 0 or 1:
    => 0 : If the patterns do not match.
    => 1 : If the patterns match.
Constraints:
1 <= length(A), length(B) <= 9e4
Examples :
Input 1:
    A = "aa"
    B = "a"
Output 1:
    0
Input 2:
    A = "aa"
    B = "aa"
Output 2:
    1
Input 3:
    A = "aaa"
    B = "aa"
Output 3:
    0
Input 4:
    A = "aa"
    B = "*"
Output 4:
    1
Input 5:
    A = "aa"
    B = "a*"
Output 5:
    1
Input 6:
    A = "ab"
    B = "?*"
Output 6:
    1
Input 7:
    A = "aab"
    B = "c*a*b"
Output 7:
    0
"""


# Think about the bruteforce solution.
# When you encounter ‘’, you would try to call the same isMatch function in the following manner:
# If p[0] == ‘’, then isMatch(s, p) is true if isMatch(s+1, p) is true OR isMatch(s, p+1) is true.
# else if p[0] is not ‘*’ and the characters s[0] and p[0] match ( or p[0] is ‘?’ ),
# then isMatch(s,p) is true only if isMatch(s+1, p+1) is true.
# If the characters don’t match isMatch(s, p) is false.
# This appraoch is exponential. Think why.
# Lets see how we can make this better. Note that isMatch function can only be called with
# suffixes of s and p. As such, there could only be length(s) * length(p) unique calls to isMatch.
# Lets just memoize the result of the calls so we only do processing for unique calls.
# This makes the time and space complexity O(len(s) * len(p)).
# There could be ways of optimizing the approach rejecting certain suffixes without processing them.
# For example, if len(non star characters in p) > len(s), then we can return false without checking anything.

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, s, p):
        if len(p) - p.count('*') > len(s):
            return 0
        DP = [True] + [False] * len(s)
        for c in p:
            if c == '*':
                for n in range(1, len(s) + 1):
                    DP[n] = DP[n - 1] or DP[n]
            else:
                for n in range(len(s) - 1, -1, -1):
                    DP[n + 1] = DP[n] and (c == s[n] or c == '?')
            DP[0] = DP[0] and c == '*'
        return 1 if DP[-1] else 0
