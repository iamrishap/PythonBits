"""
Find longest Arithmetic Progression in an integer array A of size N, and return its length.
More formally, find longest sequence of indices, 0 < i1 < i2 < … < ik < ArraySize(0-indexed) such that sequence
A[i1], A[i2], …, A[ik] is an Arithmetic Progression.
Arithmetic Progression is a sequence in which all the differences between consecutive pairs are the same,
i.e sequence B[0], B[1], B[2], …, B[m - 1] of length m is an Arithmetic Progression if and only if
B[1] - B[0] == B[2] - B[1] == B[3] - B[2] == … == B[m - 1] - B[m - 2]
Note: The common difference can be positive, negative or 0.
Input Format:
The first and the only argument of input contains an integer array, A.
Output Format:
Return an integer, representing the length of the longest possible arithmetic progression.
Constraints:
1 <= N <= 1000
1 <= A[i] <= 1e9
Examples:
Input 1:
    A = [3, 6, 9, 12]
Output 1:
    4
Explanation 1:
    [3, 6, 9, 12] form an arithmetic progression.
Input 2:
    A = [9, 4, 7, 2, 10]
Output 2:
    3
Explanation 2:
    [4, 7, 10] form an arithmetic progression.
"""


# Bruteforce solution. Let n be the length of input array. Iterate all over pairs 0 <= i < j < n and
# build Arithmetic Progression that has first two elements A[i], A[j].
# for i : [0..n - 1]
# 	for j : [i + 1..n - 1]
# 		cur = 2
# 		lst = A[j]
# 		dif = A[j] - A[i]
# 		for k : [j + 1..n - 1]
# 			if (A[k] == lst + dif)
# 				cur++
# 				lst = A[k]
# 		ans = max(ans, cur)
# It’s O(n ^ 3) solution. Think about Dynamic Programming.
# Let dp[i][j] be the length of Longest Arithmetic progression that ends in positions i and j, i.e.
# last element is A[j] and element before last is A[i]. How can we calculate a value for fixed i and j?
# We know two last elements. So we know which number should be before position i. It’s number X such that
# A[i] - X == A[j] - A[i] -> X == 2 * A[i] - A[j]. I.e we can iterate all over 0 <= k < i and
# if A[k] == X then update dp[i][j] by the value of dp[k][i] + 1(it’s easy to understand
# we only need to find rightmost such position).

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        dp = {}
        prev = A[0]
        d = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                # In Every iteration, we first check if i th index along with A[j]-A[i]
                # difference has been memoized. If yes, we add jth index along with
                # same difference as key in dp, and value is 1+dp[(i,A[j]-A[i])] and
                # remove the previous memo (to save space). If the original memo wasn't
                # present, we memoize it now.
                if (i, A[j] - A[i]) in dp:
                    dp[(j, A[j] - A[i])] = 1 + dp[(i, A[j] - A[i])]  # From ith element to jth element
                    del dp[(i, A[j] - A[i])]
                else:
                    dp[(j, A[j] - A[i])] = 1
        maxx = 0
        # we now find the maximum count
        for i in dp:
            if dp[i] > maxx: maxx = dp[i]
        return maxx + 1


A = [9, 4, 7, 2, 10]
s = Solution()
print(s.solve(A))
