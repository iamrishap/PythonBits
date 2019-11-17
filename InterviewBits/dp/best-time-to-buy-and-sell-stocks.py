"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most 2 transactions.
Return the maximum possible profit.
Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
Input Format:
The first and the only argument is an integer array, A.
Output Format:
Return an integer, representing the maximum possible profit.
Constraints:
1 <= length(A) <= 7e5
1 <= A[i] <= 1e7
Examples:
Input 1:
    A = [1, 2, 1, 2]
Output 1:
    2
Explanation 1:
    Day 0 : Buy
    Day 1 : Sell
    Day 2 : Buy
    Day 3 : Sell
Input 2:
    A = [7, 2, 4, 8, 7]
Output 2:
    6
Explanation 2:
    Day 1 : Buy
    Day 3 : Sell
"""

# What if you construct your DP space as :
# f[k, ii] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions
# How would you fill in values in f[k, ii] and how would the DP relations look like.

INF = float('inf')


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        """
        For one transaction, we can do it linearly:
        price that day - minimum seen so far.
        For two transactions, we evaluates this at day i + best for remaining days.
        """

        # Best solutions based on increasing starting days
        # We are doing it backward
        bystart = []
        high = -INF  # maximum so far
        best = 0
        for x in reversed(A):
            best = max(best, high - x)
            bystart.append(best)
            high = max(high, x)
        low = INF  # minimum so far
        best = 0
        total = 0
        for x, best2 in zip(A, reversed(bystart)):
            best = max(best, x - low)
            total = max(total, best + best2)
            low = min(low, x)
        return total
