"""
You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Note that in your output A should precede B.
Example:
Input:[3 1 2 5 3]
Output:[3, 4]
A = 3, B = 4
"""


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        seen = set()
        len_a = len(A)
        sum_a = (len_a * (len_a + 1)) // 2
        repeated = None

        for i in A:
            if i not in seen:
                seen.add(i)
                sum_a -= i
            else:
                repeated = i
        return repeated, sum_a

    def repeatedNumber2(self, A):
        n = len(A)
        x = sum(range(1, n + 1)) - sum(A)
        y = sum([i ** 2 for i in range(1, n + 1)]) - sum([i ** 2 for i in A])
        b = ((x ** 2) + y) // (2 * x)
        a = (y - (x ** 2)) // (2 * x)
        return a, b


s = Solution()
print(s.repeatedNumber2([3, 1, 2, 5, 3]))
