"""
Find out the number of N digit numbers, whose digits on being added equals to a given number S.
Note that a valid number starts from digits 1-9 except the number 0 itself. i.e. leading zeroes are not allowed.
Since the answer can be large, output answer modulo 1000000007
**
N = 2, S = 4
Valid numbers are {22, 31, 13, 40}
Hence output 4.
"""


# Part 1
# Lets build a recursive approach to this problem. Let rec_Count(id, sum) be the number of numbers having digit count
# as id and digit sum as sum. To be more clear,
# rec_Count(id, sum) = ∑ rec_Count(id-1,sum-x) where 0 <= x <= 9 && sum-x >= 0.
# Note that the above relation has not handled the leading zeroes case. How can you handle them ?
# Part 2
# We can handle them by calling this rec_Count function for the first digit explicitly. i.e. we can fix the starting
# digits from 1-9 explicitly and then call the recursion function to handle the other digits(i.e. N - 1 digits).
# Finally we can add them together to get the final answer.
# Gotcha : Try to think about the approach when sum is given as 0.
# Now, we have the recursive solution. However, the recursive solution is too
# expensive because of the exponential time complexity.
# A key thing to note here is that there are overlapping subproblems as many things are being calculated repeatedly
# in the recursive solution ? Can you use the concept of Dynamic programming to optimize the time complexity here ?
# Final solution
# My recursive function only depends on id and sum variable. If ID is the max possible id, and SUM is the max possible
# sum, then there are only ID * SUM number of ways in which the function can be called.
# We can use memoization to store those values.


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, N, S):
        arr = [[0 for j in range(S + 1)] for i in range(N + 1)]
        arr[0][0] = 1
        for n in range(N):
            for s in range(S):
                for digit in range(10):
                    if s + digit <= S:
                        arr[n + 1][s + digit] += arr[n][s]
                    else:
                        break
        return arr[N][S] % 1000000007


s = Solution()
print(s.solve(10, 16))
