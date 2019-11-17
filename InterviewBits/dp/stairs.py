"""
You are climbing a stair case and it takes A steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input Format:
The first and the only argument contains an integer A, the number of steps.
Output Format:
Return an integer, representing the number of ways to reach the top.
Constrains:
1 <= A <= 36
Example :
Input 1:
A = 2 Output 1:
2 Explanation 1:
[1, 1], [2] Input 2:
A = 3 Output 2:
3 Explanation 2:
[1 1 1], [1 2], [2 1]
"""

# This is the most basic dynamic programming problem.
# We know that we can take 1 or 2 step at a time. So, to take n steps, we must have arrived at it immediately from
# n - 1 or n-2th step.
# If we knew the number of ways to reach n-1 and n-2th step, our answer would be the summation of their number of ways.
# BONUS: Can you come up with O(logn) solution

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A > 1:
            res = [0 for i in range(A + 1)]
        elif A == 1:
            return 1
        res[0] = 1
        res[1] = 1
        for i in range(2, A + 1):
            res[i] = res[i] + res[i - 1] + res[i - 2]
        return res[A]


s = Solution()
print(s.climbStairs(3))
