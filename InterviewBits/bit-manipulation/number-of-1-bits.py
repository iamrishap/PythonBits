"""
Write a function that takes an unsigned integer and returns the number of 1 bits it has.
Example:
The 32-bit integer 11 has binary representation
00000000000000000000000000001011
so the function should return 3.
"""


# Iterate 32 times, each time determining if the ith bit is a ’1′ or not.
# This is probably the easiest solution, and the interviewer would probably not be too happy about it.
# In addition, this solution is not very efficient too because you need to iterate 32 times no matter what.
# This means that if we do (x & (x - 1)),
# it would just unset the last set bit in x (which is why x&(x-1) is 0 for powers of 2).
# x - 1 would find the first set bit from the end, and then set it to 0, and set all the bits following it.
# Which means if x = 10101001010100 then x - 1 becomes 10101001010(011)

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while A > 0:
            A &= A - 1  # When we do &, all the bits set after doing A-1 will be cleared
            count += 1
        return count
