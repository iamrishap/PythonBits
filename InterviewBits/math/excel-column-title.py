"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""


# Think of it like this.
# How would you convert a number to binary ?
# Can you apply the same principle here now that the base is different ?

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        result = []
        while A > 0:
            bit_val = A % 26  # Reduce max possible from A
            if bit_val == 0:
                bit_val = 26
            A = (A - bit_val) // 26  # Each time it is getting 26, 26**2, 26**3 ...
            result.append(chr(bit_val + 64))
        return ''.join(reversed(result))
