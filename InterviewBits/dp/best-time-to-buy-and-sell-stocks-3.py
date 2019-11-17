"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
Input Format:
The first and the only argument is an array of integer, A.
Output Format:
Return an integer, representing the maximum possible profit.
Constraints:
1 <= len(A) <= 1e5
1 <= A[i] <= 1e7
Example :
Input 1:
    A = [1, 2, 3]
Output 1:
    2
Explanation 1:
    => Buy a stock on day 0.
    => Sell the stock on day 1. (Profit +1)
    => Buy a stock on day 1.
    => Sell the stock on day 2. (Profit +1)
    Overall profit = 2
Input 2:
    A = [5, 2, 10]
Output 2:
    8
Explanation 2:
    => Buy a stock on day 1.
    => Sell the stock on on day 2. (Profit +8)
    Overall profit = 8
"""


# Observation based solution:
# Note 1: I will never buy a stock and sell it in loss.
# Note 2: If A[i] < A[i+1], I will always buy a stock on i and sell it on i+1.
# Think and try to come up with a proof on the validity of the statement.
# DP based solution:
# Let Dp[i] = max profit you can gain in region (i,i+1,….,n).
# Then Dp[i] = max(Dp[i+1],-A[i] + max( A[j]+Dp[j] st j > i ) )
# Can you come up with base cases and direction of computation now?

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        temp = []
        for i in range(len(A) - 1):
            temp.append(A[i + 1] - A[i])
        sumi = 0
        currmax = 0
        for i in range(len(temp)):
            if temp[i] > 0:
                currmax += temp[i]
            else:
                sumi += currmax
                currmax = 0
        sumi += currmax
        return sumi
