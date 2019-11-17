"""
Given a 2D matrix, find the number non-empty sub matrices, such that the sum of the elements inside the
sub matrix is equal to 0. (note: elements might be negative).
Example:
Input

-8 5  7
3  7 -8
5 -8  9
Output
2

Explanation
-8 5 7
3 7 -8
5 -8 9

-8 5 7
3 7 -8
5 -8 9
"""


# Iterate over all pairs of rows. When fixing two rows r1 and r2, we can convert this to 1D version of the problem.
# When we have a 1D array ARR we want to find number of subarrays such that the sum of the elements in the
# subarray is equal to 0. To do that lets iterate from left to right, say we are currently at i-th element.
# If we have i-th prefix sum equal to sum(ARR[0..i]), then we want to find number of such j’s
# that sum(ARR[0..i]) = sum(ARR[0..j]). That means that the subarray ARR[j + 1..i] will have zero sum.
# To efficiently count number of such j’s we can use a HashMap (unordered_map in C++).
# In order to convert the problem to 1D, when we have a pair of fixed rows r1 and r2, we will keep a 2D prefix sums,
# let’s call it PRE (let’s also assume that initial matrix is A). PRE[i, j] will be the sum of elements in sub matrix
# whose upper left corner is [0, 0] and lower right corner is [i, j]. In other words it is a sum of all A[p, q] where
# 0 <= p <= i and 0 <= q <= j.
# The calculation of PRE is very easy: PRE[i, j] = A[i, j] + PRE[i - 1, j] + PRE[i, j - 1] - PRE[i - 1, j - 1]
# (if i - 1 or j - 1 are less than 0 then we just omit the terms where they appear). Notice, that we need to
# subtract PRE[i - 1, j - 1] since it is contained in both PRE[i - 1, j] and PRE[i, j - 1] and we want every
# element to appear in PRE[i, j] exactly once. This is called inclusion exclusion principle.
# When we have two fixed rows r1, r2 and have calculated PRE, we can obtain ARR. Note that we don’t really need to
# calculate each element of ARR, since we only need prefix sums of ARR, that is sum(ARR[0..i]) for each i.
# The sum(ARR[0..i]) is equal to PRE[r2][i] - PRE[r1 - 1][i] (if r1 - 1 < 0 then omit second operand).
# Being able to efficiently calculate sum(ARR[0..i]), let’s apply the 1D solution.
# The answer to the problem will be simply the sum of answers for all different pairs of rows.
# Overall time complexity is O(N3).
# Space complexity is O(N2)


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n, m = len(A), len(A[0]) if A else 0
        if not (n and m):
            return 0
        dp_sum, ans = [[0] * (m + 1) for _ in range(n + 1)], 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp_sum[i][j] = dp_sum[i - 1][j] + dp_sum[i][j - 1] - dp_sum[i - 1][j - 1] + A[i - 1][j - 1]

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                counti = {0: 1}
                for k in range(1, m + 1):
                    val = dp_sum[j][k] - dp_sum[i - 1][k]
                    if val in counti:
                        ans = ans + counti[val]
                        counti[val] = counti[val] + 1
                    else:
                        counti[val] = 1
        return ans

    def solve_another(self, A):
        dpMap = dict()

        def presum(i, j):
            key = (i, j)
            if key in dpMap:
                return dpMap[key]
            ans = 0
            if i < 0 or j < 0:
                return 0
            ans = A[i][j] + presum(i - 1, j) + presum(i, j - 1) - presum(i - 1, j - 1)
            dpMap[key] = ans
            return ans

        N, M = len(A), len(A) and len(A[0])
        count = 0

        for i1 in range(N):
            for i2 in range(i1, N):
                countMap = defaultdict(int)
                for j in range(M):
                    s = presum(i2, j) - presum(i1 - 1, j)
                    if s == 0:
                        count += 1
                    count += countMap[s]
                    countMap[s] += 1

        return count
