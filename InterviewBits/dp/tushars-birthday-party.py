"""
As it is Tushar’s Birthday on March 1st, he decided to throw a party to all his friends at TGI Fridays in Pune.
Given are the eating capacity of each friend, filling capacity of each dish and cost of each dish.
A friend is satisfied if the sum of the filling capacity of dishes he ate is equal to his capacity. Find the minimum
cost such that all of Tushar’s friends are satisfied (reached their eating capacity).
NOTE:
Each dish is supposed to be eaten by only one person. Sharing is not allowed.
Each friend can take any dish unlimited number of times.
There always exists a dish with filling capacity 1 so that a solution always exists.
Input Format
Friends : List of integers denoting eating capacity of friends separated by space.
Capacity: List of integers denoting filling capacity of each type of dish.
Cost :    List of integers denoting cost of each type of dish.
Constraints:
1 <= Capacity of friend <= 1000
1 <= No. of friends <= 1000
1 <= No. of dishes <= 1000
Example:
Input:
    2 4 6
    2 1 3
    2 5 3
Output:
    14
Explanation:
    First friend will take 1st and 2nd dish, second friend will take 2nd dish twice.  Thus, total cost = (5+3)+(3*2)= 14
"""


# **Observations: **
# As the friends cannot share dishes, we can calculate the cost for each of them independently and add all such costs.
# Now, the problem instance for every friend is reduced to standard KnapSack problem.
# **Dynamic programming recurrence: **
# dp[i][j] –> min. cost to satisfy a person with capacity i using first j dishes.
# dp[i][j] = min( dp[i][j-1] , dp[ i-fillCap[j] ][j] + cost[j] ) // if ( i-fillCap[j] ) >= 0
# dp[i][j] = dp[i][j-1] // otherwise
# As one dish can be taken multiple times, we have used dp[ i-fillCap[j] ][ j ]
# and not dp[ i-fillCap[j] ][ j-1 ]. This is different from standard KnapSack where one element can be used only once.
# Note: Base cases should be handled properly.

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, friends, capacity, price):
        goal = max(friends)
        dp = [0] + [float("inf")] * goal

        for cap, pr in zip(capacity, price):
            for i in range(cap, goal + 1):
                cand_price = dp[i - cap] + pr
                if cand_price < dp[i]:
                    dp[i] = cand_price

        return sum(dp[friend] for friend in friends)
