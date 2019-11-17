"""
You are given a set of coins S. In how many ways can you make sum N assuming you have infinite amount of each coin in the set.
Note : Coins in set S will be unique. Expected space complexity of this problem is O(N).
Example :
Input :
    S = [1, 2, 3]
    N = 4
Return : 4
Explanation : The 4 possible ways are
{1, 1, 1, 1}
{1, 1, 2}
{2, 2}
{1, 3}
Note that the answer can overflow. So, give us the answer % 1000007
"""


# Lets say we can make the sum N - S[i] in X ways. Then if we have a coin of value S[i] we can also make a
# sum of N in X ways. We can memoize the number of ways in which we can make all the sums < N. This can be done by
# keeping a count array for all sums less than N which gives us the expected space complexity of O(N). A sum of 0
# is always possible as we can pick no coins, so the base case will be count[0] = 1
# Remember to avoid counting a way more than once. This can be done by choosing the coins in a particular order.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):
        dp = [0] * (B + 1)
        dp[0] = 1
        for coin in A:
            for i in range(1, B + 1):
                if coin <= i:
                    dp[i] = dp[i] + dp[i - coin]
        return dp[-1] % 1000007
