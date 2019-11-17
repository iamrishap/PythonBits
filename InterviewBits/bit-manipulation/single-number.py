"""
Given an array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example :
Input : [1 2 2 3 1]
Output : 3
"""

# Every number that occurs twice will either contribute 2 ‘1’s or 2 ‘0’s to the position.
# The number that occurs once-‘X’ will contribute exactly one 0 or 1 to the position
# depending on whether it has 0 or 1 in that position.
# So:
# If X has 1 in that position, we will have odd number of 1s in that position.
# If X has 0 in that position, we will have odd number of 0s in that position.

from functools import reduce


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        return reduce(lambda x, y: x ^ y, A)
