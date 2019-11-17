"""
There are A cities numbered from 1 to A. You have already visited M cities,
the indices of which are given in an array B of M integers.
If a city with index i is visited, you can visit either the city with index i-1 (i >= 2) or the city with
index i+1 (i < A) if they are not already visited.
Eg: if N = 5 and array M consists of [3, 4], then in the first level of moves, you can either visit 2 or 5.
You keep visiting cities in this fashion until all the cities are not visited.
Find the number of ways in which you can visit all the cities modulo 10^9+7.
Input Format
The 1st argument given is an integer A, i.e total number of cities.
The 2nd argument given is an integer array B, where B[i] denotes ith city you already visited.
Output Format
Return an Integer X % (1e9 + 7), number of ways in which you can visit all the cities.
Constraints
1 <= A <= 1000
1 <= M <= A
1 <= B[i] <= A
For Example
Input:
    A = 5
    B = [2, 5]
Output:
    6
Explanation:
    All possible ways to visit remaining cities are :
    1. 1 -> 3 -> 4
    2. 1 -> 4 -> 3
    3. 3 -> 1 -> 4
    4. 3 -> 4 -> 1
    5. 4 -> 1 -> 3
    6. 4 -> 3 -> 1
"""

# Brute force solution for this would create a graph and do BFS for all possible
# combinations to visit all cities. But this will result in a timeout.
# This question is simple if you understand how we are dividing the cities.
# Let’s say we start with (a_1, a_2, a_3,…, a_k) as visited cities. Let all cities be (1,2,…,n).
# Also, let’s denote cities between a_i and a_i+1 as X_i. Here, X_0 denotes cities before the first visited city.
# X_k denotes unvisited cities after a_k.
# Now there are total n-k unvisited cities. We can visit them in (n-k)! ways.
# We can not visit cities between a_i and a_i+1 in all possible ways for all i’s. We have counted all
# permutations in (n-k)!. So, we need to divide it with X_i for all i’s.
# This will lead to the expression (n-k)!/(X_0! * X_1! * … *X_k!).
# There are more than one way of visiting cities between the two visited cities. Precisely, there are 2^(X_i-1) ways
# to visit for all i. Thus we need to multiply with X_i’s.
# Here we need to remember that there is only one way to visit X_0 and X_k.
# The final formula becomes ((n-k)!/(X_0!X_2!…X_(k-1)!) )(2^(X_1 -1 + X_2 - 1 + X_3 - 1 + … + X_(k-1)-1))
# The same solution is present as the editorial for this question. You have to remember that
# ((X_0 + X_1)C(X_1))((X_0+X_1+X_3)C(X_3))….((n-k)C(X_k)) is same as ((n-k)!/(X_0!X_2!…*X_(k-1)!) ).

import sys

sys.setrecursionlimit(5000)


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def calc_combs(self, L1, C1, L2, C2, memo):
        return C1 * C2 * self.fact(L1 + L2, memo) // (self.fact(L1, memo) * self.fact(L2, memo))

    def fact(self, n, memo):
        if n in memo: return memo[n]
        if n <= 1: return 1
        v = self.fact(n - 1, memo) * n
        memo[n] = v
        return v

    def solve(self, A, B):
        if not B: return 0
        mod = 1000000007
        memo = {}
        B = sorted(B)

        # 1...B[0] has 1 possible placements of length B[0] - 1
        length, combinations = B[0] - 1, 1

        for i in range(1, len(B)):
            if B[i - 1] == B[i]: continue
            if B[i - 1] + 1 == B[i]: continue
            l = (B[i] - B[i - 1] - 1) % mod
            c = (1 << (l - 1)) % mod
            combinations = self.calc_combs(length, combinations, l, c, memo) % mod
            length += l

        # B[-1]...A has 1 possible placements of length A - B[-1]
        return self.calc_combs(length, combinations, A - B[-1], 1, memo) % mod

# TODO: Left to understand later.
