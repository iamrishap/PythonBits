"""
Given an array of integers, every element appears thrice except for one which occurs once.
Find that element which does not appear thrice.
Note: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
Example :
Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Output : 4
"""


# Let us look at every bit position.
# Every number that occurs thrice will either contribute 3 ‘1’s or 3 ‘0’s to the position.
# The number that occurs once X will contribute exactly one 0 or 1 to the position
# depending on whether it has 0 or 1 in that position.
# So:
# If X has 1 in that position, we will have (3x+1) number of 1s in that position.
# If X has 0 in that position, we will have (3x+1) number of 0s in that position.
# Having noticed that if X has 1 in that position, we will have 3x+1 number of 1s in that position.
# If X has 0 in that position, we will have 3x+1 number of 0 in that position.
# A straightforward implementation is to use an array of size 32 to keep track of the total count of ith bit.
# We can improve this based on the previous solution using three bitmask variables:
# ones as a bitmask to represent the ith bit had appeared once.
# twos as a bitmask to represent the ith bit had appeared twice.
# threes as a bitmask to represent the ith bit had appeared three times.
# When the ith bit had appeared for the third time, clear the ith bit of both ones and twos to 0.
# The final answer will be the value of ones.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for j in range(31, -1, -1):
            c = 0
            for i in A:
                if i & (1 << j):
                    c += 1  # Count the number of elements in A that has bit i set
            if c % 3 != 0:
                res |= (1 << j)
        return res
