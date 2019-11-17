"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
Return the maximum possible profit.
Input Format:
The first and the only argument is an array of integers, A.
Output Format:
Return an integer, representing the maximum possible profit.
Constraints:
1 <= len(A) <= 7e5
1 <= A[i] <= 1e7
Examples:
Input 1:
    A = [1, 2]
Output 1:
    1
Explanation:
    Buy the stock on day 0, and sell it on day 1.
Input 2:
    A = [1, 4, 5, 2, 4]
Output 2:
    4
Explanation:
    Buy the stock on day 0, and sell it on day 2.
"""


# If you buy your stock on day i, you’d obviously want to sell it on the day its price is maximum after that day.
# So essentially at every index i, you need to find the maximum in the array in the suffix.
# Now this part can be done in 2 ways :
# 1) Have another array which stores that information.
# max[i] = max(max[i+1], A[i])
# 2) Start processing entries from the end maintaining a maximum till now. Constant additional space requirement.


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        prices = A
        buy_price, profit = float('inf'), 0  # set buy_price and profit to the highest and lowest possible options
        for price in prices:
            if price < buy_price: buy_price = price  # in case you find the lowest price, set it as buy_price
            # in case profit is the highest, set it as new profit
            if price - buy_price > profit: profit = price - buy_price
        return profit
