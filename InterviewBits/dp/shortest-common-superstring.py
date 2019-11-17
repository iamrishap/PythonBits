"""
Given a set of strings, A of length N.
Return the length of smallest string which has all the strings in the set as substring.
Input Format:
The first and the only argument has an array of strings, A.
Output Format:
Return an integer representing the minimum possible length of the resulting string.
Constraints:
1 <= N <= 18
1 <= A[i] <= 100
Example:
Input 1:
    A = ["aaaa", "aa"]
Output 1:
    4
Explanation 1:
    Shortest string: "aaaa"
Input 2:
    A = ["abcd", "cdef", "fgh", "de"]
Output 2:
    8
Explanation 2:
    Shortest string: "abcdefgh"
"""


# Brute force
# Let’s say we have only two strings say s1 and s2, the possible cases are:
#
# They do not overlap [ans = len(s1) + len(s2) ]
# They overlap partially [ans = len(s1)+len(s2)-len(max. overlapping part)]
# They overlap completely [ans = max(len(s1), len(s2)]
# What we can see here is we can easily combine two strings. In the brute force, we could take all the permutations
# of numbers [1 .. N], then combine the strings in that order.
# e.g: strings = [s1, s2, s3], order = [2,3,1]
# Steps are: [s1, s2,s3] –> [s2+s3, s1] –> [s1+s2+s3].
# (Here addition of strings is according to the method described above.
# I would advice you to completely digest that this will give the optimal solution whatever the case may be.
# Considering all the permutations is optimal but time consuming.
#
# Dynamic programming
# We have dynamic programming to our rescue in this case. You can see that there is a optimal substructure and
# overlapping subproblems in the brute force algorithm described above. Well if you can’t already see,
# let me help you out. Example:
# Input = [s1, s2, s3, s4]
# Order 1 = [2,3,1,4] , Steps: [s2+s3, s1, s4] –> [s2+s3+s1, s4] –> [s1+s2+s3+s4]
# Order 2 = [1,3,2,4] , Steps: [s1+s3, s2, s4] –> [s1+s2+s3, s4] –> [s1+s2+s3+s4].
#
# Do you see here that Order1 and Order2 both calculated the optimal solution for set of strings [s1, s2, s3]
# (Intermediate string s1+s2+s3 is the optimal solution for this set)
#
# Hurrah! Time to think Dynamically.
#
# Bitmasking in DP
# Well, this kind of DP formulations require a specific technique called Bitmasking. It is not the conventional type
# and in this case T(N) = CCNN + CN*(2^N) (Still better than O(N!) right).
#
# Formulation:
# dp[i][mask] = Optimal solution for set of strings corresponding to 1’s in the mask where the last added string to
# our solution is i-th string.
# Recurrence:
# dp[i][mask] = min(dp[x][mask ^ (1«i)] where {mask | (1«x) = 1} )
# I recommend you reading about the Bitmask in DP if you still have the doubt.

class Solution:

    def substring(self, a, b):
        if a.find(b) != -1:
            return b
        elif b.find(a) != -1:
            return a
        return None

    def overlap(self, a, b):
        l1 = self.overlap_length(a, b)
        l2 = self.overlap_length(b, a)
        if l1 > l2:
            return l1, a, b
        else:
            return l2, b, a

    def overlap_length(self, a, b):
        length = 0
        for i in range(len(a)):
            x = len(a) - i
            if a[x:] == b[:i]:
                length = i
        return length

    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        a = [i for i in A]

        while len(a) > 1:
            item_to_remove = None
            max_overlap = None
            for i in range(len(a)):
                for j in range(i + 1, len(a)):
                    item_to_remove = self.substring(a[i], a[j])
                    if item_to_remove is not None:
                        break

                    length, first, second = self.overlap(a[i], a[j])
                    if not max_overlap or max_overlap[0] < length:
                        max_overlap = length, first, second

                if item_to_remove is not None:
                    a.remove(item_to_remove)
                    break

            # print max_overlap
            if max_overlap is not None:
                length, first, second = max_overlap
                a.remove(first)
                a.remove(second)
                a.append(first + second[length:])

        return len(a[0])


# TODO: Mind is off. Didn't grasp this. Revisit.
