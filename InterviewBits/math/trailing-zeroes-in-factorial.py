"""
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
Example :
n = 5
n! = 120
Number of trailing zeros = 1
So, return 1
"""

# For given number 4617.
# 5^1 : 4617 ÷ 5 = 923.4, so we get 923 factors of 5
# 5^2 : 4617 ÷ 25 = 184.68, so we get 184 additional factors of 5
# 5^3 : 4617 ÷ 125 = 36.936, so we get 36 additional factors of 5
# 5^4 : 4617 ÷ 625 = 7.3872, so we get 7 additional factors of 5
# 5^5 : 4617 ÷ 3125 = 1.47744, so we get 1 more factor of 5
# 5^6 : 4617 ÷ 15625 = 0.295488, which is less than 1, so stop here.
# Therefore, 4617! has 923 + 184 + 36 + 7 + 1 = 1151 trailing zeroes.

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        # Zero is formed by 2*5.
        # No. of 2's always > No. of 5's in factorial of a number.
        # Therefore, counting the No. of 5's gives the number of trailing zeros
        # If A < 5 then its factorial doesn't have any trailing zeros
        if A < 5:
            return 0
        count = 0
        i = 5
        while (A // i > 0):
            count += A // i
            i *= 5
        return count
