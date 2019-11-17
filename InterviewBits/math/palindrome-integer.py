"""
Determine whether an integer is a palindrome. Do this without extra space.
A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.
Example :
Input : 12121
Output : True
Input : 123
Output : False
"""

# Figure out how to extract digit at ith place using some mathematics without using extra space.
# Corner cases to consider:
# 1) Negative numbers
# 2) If you are thinking of converting the integer to string, note the restriction of using extra space.
# 3) Try reversing the integer.

import math


class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        rev = 0
        num = A
        while num > 0:
            temp = num % 10
            rev = rev * 10 + temp
            num = math.floor(num / 10)
        if A == rev:
            return 1
        else:
            return 0
