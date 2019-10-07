'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        revstr = ''.join(str(x)[::-1])
        revint = int(revstr) if revstr[-1] != '-' else int('-' + revstr[:-1])
        return revint if revint <= 2147483647 and revint >= -2147483648 else 0

    def reverse_nicely(self, x):
        s = (x > 0) - (x < 0)  # get sign
        r = int(repr(s * x)[::-1])
        return (r < 2 ** 31) * s * r

s = Solution()
print(s.reverse_nicely(-8389199))