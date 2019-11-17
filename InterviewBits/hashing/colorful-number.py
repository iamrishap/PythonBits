"""
For Given Number N find if its COLORFUL number or not
Return 0/1
COLORFUL number:
A number can be broken into different contiguous sub-subsequence parts.
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Example:
N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different.
Output : 1
"""

# Note that input number can be of length atmax 10.
# So, number of substring can be atmax 45.
# It is one of the easiest problem in this section.
# You just need to simulate what has been stated in the problem.
# Iterate over all substrings of number, and then check if the number
# resulting from the multiplication has been stored by us or not using hashing.
# Example:
# N = 123
# 1 2 3 12 23 123
# 1 -> 1
# 2 -> 2
# 3 -> 3
# 12 -> 2  uh-oh, we have already encountered 2 before. Return 0

from functools import reduce


class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        products = set()
        str_num = str(A)
        for i in range(len(str_num)):
            for j in range(i + 1, len(str_num) + 1):
                product = reduce(lambda x, y: x * y, map(int, list(str_num[i:j])))
                if product in products:
                    return 0
                products.add(product)
        return 1
