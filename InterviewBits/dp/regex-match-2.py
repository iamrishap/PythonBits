"""
Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
The function prototype should be:
int isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") → 0
isMatch("aa","aa") → 1
isMatch("aaa","aa") → 0
isMatch("aa", "a*") → 1
isMatch("aa", ".*") → 1
isMatch("ab", ".*") → 1
isMatch("aab", "c*a*b") → 1
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# This looks just like a straight forward string matching, isn’t it? Couldn’t we just match the pattern and the input
# string character by character? The question is, how to match a '*' ?
# A natural way is to use a greedy approach; that is, we attempt to match the previous character as many as we can.
# Does this work? Let us look at some examples.
# s = “abbbc”
# p = “ab*c”
# Assume we have matched the first ‘a’ on both s and p. When we see "b*" in p, we skip all b’s in s. Since the
# last ‘c’ matches on both side, they both match.
# s = “ac”
# p = “ab*c”
# After the first ‘a’, we see that there is no b’s to skip for “b*”. We match the last ‘c’ on both side and
# conclude that they both match.
# It seems that being greedy is good. But how about this case?
# s = “abbc”
# p = “ab*bbc”
# When we see “b*” in p, we would have skip all b’s in s. They both should match, but we have no more b’s to match.
# Therefore, the greedy approach fails in the above case.
# One might be tempted to think of a quick workaround. How about counting the number of consecutive b’s in s? If it
# is smaller or equal to the number of consecutive b’s after “b*” in p, we conclude they both match and continue from
# there. For the opposite, we conclude there is not a match.
# This seem to solve the above problem, but how about this case:
# s = “abcbcd”
# p = “a.*c.*d”
# Here, “.*” in p means repeat ‘.’ 0 or more times. Since ‘.’ can match any character, it is not clear how many times
# ‘.’ should be repeated. Should the ‘c’ in p matches the first or second ‘c’ in s? Unfortunately, there is no way
# to tell without using some kind of exhaustive search.
# We need some kind of backtracking mechanism such that when a matching fails, we return to the last successful matching
# state and attempt to match more characters in s with ‘*’. This approach leads naturally to recursion.
# The recursion mainly breaks down elegantly to the following two cases:
# If the next character of p is NOT ‘*’, then it must match the current character of s. Continue pattern matching
# with the next character of both s and p.
# If the next character of p is ‘*’, then we do a brute force exhaustive matching of 0, 1, or more repeats of current
# character of p… Until we could not match any more characters.
# You would need to consider the base case carefully too. That would be left as an exercise to the reader. :)

class Solution:
    def isMatch(self, A, B, index_s=0, index_r=0):
        while index_s < len(A) and index_r < len(B):
            if B[index_r] == '.':
                if index_r + 1 < len(B) and B[index_r + 1] == '*':
                    for i in range(index_s, len(A) + 1):
                        if self.isMatch(A, B, i, index_r + 2):
                            return 1
                    return 0
                else:
                    index_s += 1
                    index_r += 1
            else:
                ch = B[index_r]
                if index_r + 1 < len(B) and B[index_r + 1] == '*':
                    for i in range(index_s, len(A) + 1):
                        if i > index_s and A[i - 1] != ch:
                            break
                        if self.isMatch(A, B, i, index_r + 2):
                            return 1
                    return 0
                else:
                    if ch == A[index_s]:
                        index_r += 1
                        index_s += 1
                    else:
                        return 0
        if index_s == len(A) and index_r == len(B):
            return 1
        if index_s == len(A) or index_r == len(B):
            return 0
