"""
Reverse bits of an 32 bit unsigned integer
Example 1:
x = 0,
          00000000000000000000000000000000
=>        00000000000000000000000000000000
return 0
Example 2:
x = 3,
          00000000000000000000000000000011
=>        11000000000000000000000000000000
return 3221225472
"""


# How do you swap the ‘i’th bit with the ‘j’th bit?
# Try to figure out if you could use the XOR operation to do it.
# 0 ^ 0 == 0,
# 1 ^ 1 == 0,
# 0 ^ 1 == 1, and
# 1 ^ 0 == 1.
# We only need to perform the swap when the ‘i’th bit and the ‘j’th bit are different.
# To test if two bits are different, we could use the XOR operation. Then, we need to toggle both ‘i’th and ‘j’th bits.
# We could apply the XOR operation again.
# By XOR-ing the ‘i’th and ‘j’th bit with 1, both bits are toggled.

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        result = 0
        n = 32
        for i in range(n):
            if (A >> i) & 1: result |= 1 << (n - 1 - i)
        return result

# TODO: Implement based on the approach given in the hint
