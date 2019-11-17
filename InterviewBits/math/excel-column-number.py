"""
Given a column title as appears in an Excel sheet, return its corresponding column number.
Example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""


# Simple math.
# This is just like base 26 number conversion.
# number = 26^0 * (S[n - 1] - ‘A’ + 1) + 26^1 * (S[n - 2] - ‘A’ + 1) + ….

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        T = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))  # Elegantly done
        return sum(T[ch] * 26 ** i for i, ch in enumerate(A[::-1]))
