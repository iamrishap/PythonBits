"""
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code,
print the sequence of gray code. A gray code sequence must begin with 0.
For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2
There might be multiple gray code sequences possible for a given n.
Return any such sequence.
"""


# The bruteforce method would be to start with 0, change any of the bits, keeping track of the numbers
# already constructed. When you run into a number where there is no way forward possible, you backtrack,
# and try to change some other bit instead. This might however be inefficient.
# You can notice that if a sequence is gray code, then its reverse is also a gray code.
# Where 0G(n) means all elements of G(n) prefixed with 0 bit and 1R(n) means all elements of R(n) prefixed with 1.
# Note that last element of G(n) and first element of R(n) is same.

class Solution:
    # input: length of binary words
    # output: list of integers in gray code
    def grayCode(self, n):
        gray_seq = [0, 1]  # gray code for n=1
        for i in range(1, n):  # recursivley extending for n>1
            # 2 ** i gives us 2, 4, 8 ...
            # Reversing at each iteration
            gray_seq += [s + 2 ** i for s in reversed(gray_seq)]
        return gray_seq


s = Solution()
print(s.grayCode(3))
