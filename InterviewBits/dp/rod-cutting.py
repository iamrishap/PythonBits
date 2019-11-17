"""
There is a rod of length N lying on x-axis with its left end at x = 0 and right end at x = N. Now, there are M weak
 points on this rod denoted by positive integer values(all less than N) A1, A2, …, AM. You have to cut rod at all
 these weak points. You can perform these cuts in any order. After a cut, rod gets divided into two smaller sub-rods.
 Cost of making a cut is the length of the sub-rod in which you are making a cut.
Your aim is to minimise this cost. Return an array denoting the sequence in which you will make cuts. If two different
sequences of cuts give same cost, return the lexicographically smallest.
Notes:
Sequence a1, a2 ,…, an is lexicographically smaller than b1, b2 ,…, bm, if and only if at the first i where ai and bi
differ, ai < bi, or if no such i found, then n < m.
N can be upto 109.
For example,
N = 6
A = [1, 2, 5]
If we make cuts in order [1, 2, 5], let us see what total cost would be.
For first cut, the length of rod is 6.
For second cut, the length of sub-rod in which we are making cut is 5(since we already have made a cut at 1).
For third cut, the length of sub-rod in which we are making cut is 4(since we already have made a cut at 2).
So, total cost is 6 + 5 + 4.
Cut order          | Sum of cost
(lexicographically | of each cut
 sorted)           |
___________________|_______________
[1, 2, 5]          | 6 + 5 + 4 = 15
[1, 5, 2]          | 6 + 5 + 4 = 15
[2, 1, 5]          | 6 + 2 + 4 = 12
[2, 5, 1]          | 6 + 4 + 2 = 12
[5, 1, 2]          | 6 + 5 + 4 = 15
[5, 2, 1]          | 6 + 5 + 2 = 13
So, we return [2, 1, 5].
"""

# We rewrite our problem as given N cut points(and you cannot make first and last cut), decide order of these cuts
# to minimise the cost. So, we insert 0 and N at beginning and end of vector B. Now, we have solve our new problem
# with respect to this new array(say A).
# We define dp(i, j) as minimum cost for making cuts Ai, Ai+1, …, Aj. Note that you are not making cuts Ai and Aj,
# but they decide the cost for us.
# For solving dp(i, j), we iterate k from i+1 to j-1, assuming that the first cut we make in this interval is Ak.
# The total cost required(if we make first cut at Ak) is Aj - Ai + dp(i, k) + dp(k, j).
# This is our solution. We can implement this DP recursively with memoisation. Total complexity will be O(N3).
# For actually building the solution, after calculating dp(i, j), we can store the index k which gave the minimum
# cost and then we can build the solution backwards.
from functools import wraps


def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrap


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def rodCut(self, n, A):
        A = tuple(A)
        return self.recurse(A, 0, n)[1]

    @memo
    def recurse(self, A, left, right):
        if not len(A):
            return 0, []
        elif len(A) == 1:
            return right - left, [A[0]]
        else:
            mi = 999999999999
            min_sequence = None
            for i, a in enumerate(A):
                l = self.recurse(A[:i], left, a)
                r = self.recurse(A[i + 1:], a, right)
                tot = l[0] + r[0] + (right - left)
                if tot < mi:
                    mi = tot
                    min_sequence = (tot, [a] + l[1] + r[1])
            return min_sequence
