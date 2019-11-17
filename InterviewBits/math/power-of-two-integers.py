"""
Given a positive integer which fits in a 32 bit signed integer,
find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.
Example
Input : 4
Output : True
as 2^2 = 4.
"""


# Lets look at the number of valid possibilities for A^B.
# For B = 2, number of possibilities = sqrt(INT_MAX) = sqrt(2^31 - 1) < 2^16.
# For B = 3, number of possibilities = INT_MAX**1/3 < 2^11
# For B = 4, number of possibilities = INT_MAX**1/4 < 2^8
# .
# .
# For B = 32, number of possibilities = 0
# ( Not considering 1 as its considered in the first case, and 2^32 exceeds INT_MAX ).
# So, the total number of possibilities are less than 10^5.
# Now, we just need to iterate on these possibilities and see if we find X = A^B.
# Take extra care to make sure there are no overflows.

class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        from math import log, sqrt
        if A == 1:
            return 1
        for i in range(2, int(sqrt(A)) + 1):
            # For each i it will check if A can be represented as a power of 2, 3, 4, 5 ...
            x = round(log(A, i), 5)  # Returns rounded to 5 decimals places
            if x % 1 == 0:  # If not modulo, it is a power
                return 1
        return 0


s = Solution()
print(s.isPower(27))
