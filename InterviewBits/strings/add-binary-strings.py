"""
Given two binary strings, return their sum (also a binary string).
Example:
a = "100"
b = "11"
Return a + b = “111”
"""


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, x, y):

        max_len = max(len(x), len(y))
        x = x.zfill(max_len)  # zfill is useful here
        y = y.zfill(max_len)

        result = ''
        carry = 0

        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1

        if carry != 0: result = '1' + result
        return result.zfill(max_len)
