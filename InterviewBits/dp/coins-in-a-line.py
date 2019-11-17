"""
There are A coins (Assume A is even) in a line.
Two players take turns to take a coin from one of the ends of the line until there are no more coins left.
The player with the larger amount of money wins.
Assume that you go first.
Return the maximum amount of money you can win.
Input Format:
The first and the only argument of input contains an integer array, A.
Output Format:
Return an integer representing the maximum amount of money you can win.
Constraints:
1 <= length(A) <= 500
1 <= A[i] <= 1e5
Examples:
Input 1:
    A = [1, 2, 3, 4]
Output 1:
    6
Explanation 1:
    You      : Pick 4
    Opponent : Pick 3
    You      : Pick 2
    Opponent : Pick 1
    Total money with you : 4 + 2 = 6
Input 2:
    A = [5, 4, 8, 10]
Output 2:
    15
Explanation 2:
    You      : Pick 10
    Opponent : Pick 8
    You      : Pick 5
    Opponent : Pick 4
    Total money with you : 10 + 5 = 15
"""


# So, the question is what’s the recurrence relation for this problem
# Rec(player = you, start, end) =
# 	    |
# 	max | v(end) + Rec(opposite_player, start, end - 1)
# 	    |
# 	    | v(start) + Rec(opposite_player, start + 1, end)
# 	    |
# Rec(player = opposite, start, end) =
# 	    |
# 	min | Rec(you, start, end - 1)
# 	    |
# 	    | Rec(you, start + 1, end)
# 	    |
# now can you define base cases and memorize it ?


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        '''
        Solution by dynamic programming.
           dp[i][j] = maximum score possible for current player for subgame A[i:j]
        Base cases, only one option:
           dp[i][i+1] = A[i]
        Otherwise, we pick at either end, eventually getting
        all the coins but the ones picked by next player:
           dp[i][j] = sum(A[i:j]) - min(dp[i+1][j], dp[i][j-1])

        Now, we only have to maintain one column (j-1) to obtain new one (j).

        Time: O(n**2)   Space: O(n)
        '''

        n = len(A)
        dp = [None] * n

        for j in range(1, n + 1):
            dp[j - 1] = A[j - 1]  # dp[j-1][j]
            total = A[j - 1]
            # dp[i+1][j] must be already computed, so we iterate backward
            for i in range(j - 2, -1, -1):
                total += A[i]  # sum[i:j]
                dp[i] = total - min(dp[i + 1], dp[i])

        return dp[0]
