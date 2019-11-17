"""
Divide two integers without using multiplication, division and mod operator.
Return the floor of the result of the division.
Example:
5 / 2 = 2
Also, consider if there can be overflow cases. For overflow case, return INT_MAX.
"""


# dividend = answer * divisor + c
# You need to find the answer here without using any of the operators mentioned in the question.
# Think about the binary expansion of answer.
# Think in terms of bits.
# How do you do the division with bits?
# How do you determine the most significant bit in the answer?
# Iterate on the bit position ‘i’ from 31 to 1 and find the first bit for which divisor«i is less than dividend.
# How do you use (1) to move forward in similar fashion?

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, dividend, divisor):
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        res = 0
        p = abs(dividend)
        q = abs(divisor)
        if divisor == 0 or (divisor == 1 and dividend >= INT_MAX):
            return INT_MAX
        if dividend <= INT_MIN and divisor == -1:
            return INT_MAX
        if abs(divisor) == 1:
            return dividend * divisor
        while p >= q:
            c = 0
            while p > (q << c):
                c += 1
            res += 1 << (c - 1)
            p -= q << (c - 1)

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return res
        else:
            return -res

# TODO: Left as it is complicated. Revisit.
