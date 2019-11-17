"""
Given a string s, partition s such that every string of the partition is a palindrome.
Return all possible palindrome partitioning of s.
For example, given s = "aab",
Return
  [
    ["a","a","b"]
    ["aa","b"],
  ]
 Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
*
*
*
(len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
In the given example,
["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
"""


# Since, we are listing out all the partitions ( and not counting them), we need to do brute force here.
# When on index i, you incrementally check all substring starting from i for being palindromic.
# If found, you recursively solve the problem for the remaining string and add it to your solution.
# Start this recursion from starting position of the string.
# PS: You can optimize your solution by not computing the answer for same index multiple times using DP.

class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        def checkpal(S):
            return S == S[::-1]

        def recur(S, res, cur):
            if len(S) == 0:
                res += [cur]
            else:
                for i in range(1, len(S) + 1):
                    if checkpal(S[:i]):
                        recur(S[i:], res, cur + [S[:i]])  # cur + [S[:i]] will append this palen and find a bigger one

        res = []
        recur(A, res, [])
        return res


s = Solution()
print(s.partition('aaabc'))
